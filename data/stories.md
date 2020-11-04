## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## survey happy path
* greet
  - utter_greet
* affirm
<!-- activate form -->
  - health_form
  - form{"name":"health_form"}  
<!-- deactivate form assuming all slot values are filled -->
  - form{"name":"null"} 
  - utter_slots_values
  - utter_complete_form
* thankyou
  - utter_no_worries
  - utter_goodbye

## survey happy path 2
* greet
  - utter_greet
* affirm
<!-- activate form -->
  - health_form
  - form{"name":"health_form"}  
<!-- deactivate form assuming all slot values are filled -->
  - form{"name":"null"} 
  - utter_slots_values
  - utter_complete_form
* ask_food_associated_condition
  - utter_dietary_info
* thankyou
  - utter_no_worries
  - utter_goodbye

## survey stop
* greet
  - utter_greet
* affirm
<!-- activate form -->
  - health_form
  - form{"name":"health_form"}  
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name":"null"} 
  - utter_goodbye

## survey continue
* greet
  - utter_greet
* affirm
<!-- activate form -->
  - health_form
  - form{"name":"health_form"}  
* out_of_scope
  - utter_ask_continue
* affirm
  - health_form
  - form{"name":"health_form"}  
  - utter_slots_values
  - utter_complete_form

## no survey
* greet
  - utter_greet
* deny
  - utter_goodbye

 ## ask health questions form
* greet
  - utter_greet
* affirm
  - health_form
  - form{"name":"health_form"}    
* ask_exercise
  - utter_ask_condition
  - health_form
  - form{"name":"null"}  
  - utter_complete_form
  


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## ask food associated questions  
* ask_food_associated_condition
- utter_foods_to_avoid

## ask dietary changes  
* ask_dietary_changes
- utter_foods_to_avoid

## ask vitamins 
* ask_vitamins
- utter_vitamins_info

## ask gluten
* ask_gluten
- utter_gluten_info

## ask sugar
* ask_sugar
- utter_sugar_info

## ask dairy
- ask_dairy
- utter_dairy_info

## ask corn
* ask_corn
- utter_corn_info

## ask artificial ingredients
* ask_artificial_ingredients
- utter_artificial_ingredients_info

