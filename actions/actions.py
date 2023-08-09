from typing import Coroutine, List, Dict, Any, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.types import DomainDict

# class CustomActionCheckEmptySlots(Action):
#     def name(self) -> Text:
#         return "action_check_empty_slots"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Get the current slot values
#         current_slots = tracker.slots

#         # print(current_slots.items())


#         # Check each slot for emptiness
#         for slot_name, slot_value in current_slots.items():
#             print(slot_name)
#             if slot_value is None:
#                 print("Rewrite ")

#         else:
#             dispatcher.utter_message("All slots have been filled.")

#         return []


# class CustomActionHotelPlace(Action):
#     def name(Self) -> Text:
#         return "action_hotel_place"
    
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain:Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         data=[{"label":"Pokhara","value":"/hotel_location{'hotel_palce':'Pokhara'}"},{"label":"Kathmandu","value":"/hotel_location{'hotel_place':'Kathmandu'}"},
#               {"label":"Chitwan","value":"/hotel_location{'hotel_place':'chitwan'}"}]
#         message={"payload":"dropDown","data":data}
#         print(message)
#         dispatcher.utter_message(text="Select a Place:",json_message=message)

#         return []
