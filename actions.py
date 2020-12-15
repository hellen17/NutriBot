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
#from rasa_core.events import SlotSet

import requests
import json
import os 

#global variables
rate = 0
need = 0
weight = 0
height = 0
age = 0
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
         return ["condition", "age", "medication", "gender", "height", "weight", "meal"]
        

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
        
            "condition": [
                self.from_text(intent="inform"),
                self.from_entity(entity="condition"),
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



class CalculateCalorieIntakeAction(Action):
 def name(self):
  """name of the custom action"""
  return "action_calculate_calorie_intake"

 def run(self,dispatcher,tracker,domain):
  height = tracker.get_slot('height')
  weight = tracker.get_slot('weight')
  gender = tracker.get_slot('gender')
  meal = tracker.get_slot('meal')

# if the user is male, use the bmr formula for men
  if gender == "male":
    rate = 66.473 + (13.7516 * int(weight)) + (5.0003 * int(height)) - (6.7550 * int(age))
# if the user is female, use the bmr formula for women     
  if gender == "female": 
    rate = 655.0955 + (9.5634 * int(weight)) + (1.8496 * int(height)) - (4.6756 * int(age))

  message = "Without any activity, your body burns %s calories everyday" %rate
  #message="BOOKING DETAILS:"+"\n\n"+"Checkin Date:"+check_in+"\n"+"Checkout Date:"+check_out+"\n"+"No. of Adults:"+adults+"\n"+"No. of Children:"+child+"\n"+"No.of Rooms:"+room+"\n"+"Phone Number:"+phno+"\n"+"Email:"+email
  dispatcher.utter_message(message)  

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

