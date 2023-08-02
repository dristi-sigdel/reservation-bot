# from typing import Text, Dict, Any, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionFlightLocation(Action):
#     def name(self) -> Text:
#         return "action_flight_location"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         source_entity = None
#         destination_entity = None

#         for entity in tracker.latest_message['entities']:
#             role = entity['role']
#             value = entity['value']

#             if role == 'source':
#                 source_entity = value
#             elif role == 'destination':
#                 destination_entity = value

#         # Do something with the extracted source and destination entities
#         if source_entity and destination_entity:
#             # Perform the action based on source and destination
#             pass

#         return []
