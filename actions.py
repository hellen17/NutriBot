# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from dotenv import load_dotenv

import requests
import json
import os 

class UserForm(FormAction):


    def name(self):
        return "user_form"

    @staticmethod
    def required_slots(tracker):

        # if tracker.get_slot('name') == True:
        #     return ["name", "condition", "medication",
        #      "age"]
        # else:
        #     return ["condition", "age", "medication"]
         return ["name", "condition", "age", "medication", "gender", "height", "weight", "meal"]
        

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

            # response = create_health_log(
            #     tracker.get_slot("confirm_exercise"),
            #     tracker.get_slot("exercise"),
            #     tracker.get_slot("sleep"),
            #     tracker.get_slot("stress"),
            #     tracker.get_slot("diet"),
            #     tracker.get_slot("goal")
            # )

            # dispatcher.utter_message("Thanks, your answers have been recorded!")

            return []



    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        # """A dictionary to map required slots to
        #     - an extracted entity
        #     - intent: value pairs
        #     - a whole message
        #     or a list of them, where a first match will be picked"""

        return {
            "name": [

                self.from_text(intent="inform"),
                # self.from_entity(entity="sleep"),
                # self.from_intent(intent="deny", value="None"),
            ],
            "condition": [
                self.from_text(intent="inform"),
            ],
            "age": [
                self.from_text(intent="inform"),

                # self.from_text(intent="inform"),
                # self.from_text(intent="affirm"),
                # self.from_text(intent="deny"),
            ],
            "medication": [
                self.from_text(intent="inform"),
                self.from_intent(intent="deny", value="None"),
                self.from_intent(intent="affirm", value=True),

            ],

            "gender": [
                self.from_text(intent="inform"),
            ],
            
            "height": [
                self.from_text(intent="inform"),
            ],
            "weight": [
                self.from_text(intent="inform"),
            ],
            "meal": [
                self.from_text(intent="inform"),
            ],
        }

#calorie
# class CalorieForm(FormAction):


#     def name(self):
#         return "calorie_form"

#     @staticmethod
#     def required_slots(tracker):

#         # if tracker.get_slot('name') == True:
#         #     return ["name", "condition", "medication",
#         #      "age"]
#         # else:
#         #     return ["condition", "age", "medication"]
#          return ["meal"]
        

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:

#             # response = create_health_log(
#             #     tracker.get_slot("confirm_exercise"),
#             #     tracker.get_slot("exercise"),
#             #     tracker.get_slot("sleep"),
#             #     tracker.get_slot("stress"),
#             #     tracker.get_slot("diet"),
#             #     tracker.get_slot("goal")
#             # )

#             # dispatcher.utter_message("Thanks, your answers have been recorded!")

#             return []



#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         # """A dictionary to map required slots to
#         #     - an extracted entity
#         #     - intent: value pairs
#         #     - a whole message
#         #     or a list of them, where a first match will be picked"""

#         return {
#             "name": [

#                 self.from_text(intent="inform"),
#                 # self.from_entity(entity="sleep"),
#                 # self.from_intent(intent="deny", value="None"),
#             ],
#             "condition": [
#                 self.from_text(intent="inform"),
#             ],
#             "age": [
#                 self.from_text(intent="inform"),

#                 # self.from_text(intent="inform"),
#                 # self.from_text(intent="affirm"),
#                 # self.from_text(intent="deny"),
#             ],
#             "medication": [
#                 self.from_text(intent="inform"),
#                 self.from_intent(intent="deny", value="None"),
#                 self.from_intent(intent="affirm", value=True),

#             ],
#         }

