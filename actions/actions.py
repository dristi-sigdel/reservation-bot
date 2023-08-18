from typing import Coroutine, List, Dict, Any, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet, FollowupAction

from actions import data


class ActionHotel(Action):
    def name(self) -> Text:
        return "action_hotel"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {'payload' : '/hotel_pkr{"hotel_place":"Pokhara"}', 'title':'Pokhara' },
            {'payload' : '/hotel_chitwan{"hotel_place":"chitwan"}', 'title':'Chitwan' },
            {'payload' : '/hotel_ktm{"hotel_place":"Kathmandu"}', 'title':'Kathmandu' }
        ]

        dispatcher.utter_message(text="Which palce would you like to book a hotel from?", buttons = buttons)
        return[]

class HotelLocationAction(Action):
    def name(self) -> Text:
        return "action_hotel_place"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # hotel_place = tracker.latest_message['text']
        # print(hotel_place)
        # return [SlotSet("user_name", hotel_place)]

        slot_value = (tracker.get_slot("hotel_place")).lower()

        if slot_value:
            hotels = data.check_available(slot_value)

            if hotels:
                dispatcher.utter_message(f"{hotels}")
            else:
                dispatcher.utter_message("The location is not available.")
            
        else:
            dispatcher.utter_message("Choose the location of the hotel: ")


class ClearSlotsAction(Action):
    def name(self) -> Text:
        return "action_clear_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Clear all slots
        slots_to_clear = tracker.slots.keys()
        slot_events = [SlotSet(slot, None) for slot in slots_to_clear]
        
        # Return the slot events to clear all slots
        return slot_events