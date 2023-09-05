from typing import Coroutine, List, Dict, Any, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, FollowupAction

# from actions import data
import data
import psycopg2
import json

# Low-level connection using psycopg2
def data_fetch(loc):
    try:
        conn = psycopg2.connect(
        host="localhost",
        database="rasa",
        user="postgres",
        password="123456789"
        )

        cursor = conn.cursor()

        cursor.execute("SELECT name, rating, price, location FROM hotel WHERE location = %s;", (loc,))
        records = cursor.fetchall()

        print(records)



        column_names = [desc[0] for desc in cursor.description]
        formatted_data = [dict(zip(column_names, row)) for row in records]
        json_data = json.dumps(formatted_data)
        
        cursor.close()
        conn.close()

        return json_data

    except psycopg2.Error as e:
        return "Error: Unable to connect"


data_fetch('pokhara')

class ActionHotel(Action):
    def name(self) -> Text:
        return "action_hotel"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        places = [
            {'label' : "Pokhara", "value":"/hotel_pkr{'hotel_place:'Pokhara}"},
            {'label' : "Kathmandu", "value":"/hotel_ktm{'hotel_place:'Kathmandu}"},
            {'label' : "Chitwan", "value":"/hotel_ctwn{'hotel_place:'Chitwan}"}
        ]

        message={"payload":"dropDown","data":places}

        dispatcher.utter_message(text="Which palce would you like to book a hotel from?", json_message=message)
        return[]

# class HotelLocationAction(Action):
#     def name(self) -> Text:
#         return "action_hotel_place"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # hotel_place = tracker.latest_message['text']
#         # print(hotel_place)
#         # return [SlotSet("user_name", hotel_place)]

#         slot_value = (tracker.get_slot("hotel_place")).lower()

#         if slot_value:
#             hotels = data.check_available(slot_value)

#             if hotels:
#                 dispatcher.utter_message(f"{hotels}")
#             else:
#                 dispatcher.utter_message("The location is not available.")
            
#         else:
#             dispatcher.utter_message("Choose the location of the hotel: ")

class HotelsAction(Action):
    def name(self) -> Text:
        return "action_hotel_place"
    
    def run(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_value = (tracker.get_slot("hotel_place")).lower()

        data = {
            "payload": 'cardsCarousel',
            "data": data_fetch(slot_value)
        }
        
        dispatcher.utter_message(json_message=data)



class ClearSlotsAction(Action):
    def name(self) -> Text:
        return "action_clear_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear all slots
        slots_to_clear = tracker.slots.keys()
        slot_events = [SlotSet(slot, None) for slot in slots_to_clear]
        
        # Return the slot events to clear all slots
        return slot_events
    