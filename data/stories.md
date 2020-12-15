## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy


<!-- ## survey happy path
* greet
  - utter_greet
* calorie_intake
  - utter_ask_condition
* condition
  - utter_ask_age 
* age
  - utter_ask_gender
* gender
  - utter_ask_height
* height
  - utter_ask_weight    
* weight 
  - utter_ask_meal
* meal
  - action_calculate_calorie_intake -->


## survey happy path
* greet
  - utter_greet
* calorie_intake
<!-- activate form -->
  - user_form
  - form{"name":"user_form"}  
<!-- deactivate form assuming all slot values are filled -->
  - form{"name":"null"} 
  - utter_slots_values
  - action_calculate_calorie_intake
  - utter_complete_form
* thankyou
  - utter_no_worries
  - utter_goodbye

## survey happy path 2
* greet
  - utter_greet
* calorie_intake
<!-- activate form -->
  - user_form
  - form{"name":"user_form"}  
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
* calorie_intake
<!-- activate form -->
  - user_form
  - form{"name":"user_form"}  
* out_of_scope
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name":"null"} 
  - utter_goodbye

## survey continue
* greet
  - utter_greet
* calorie_intake
<!-- activate form -->
  - user_form
  - form{"name":"user_form"}   
* out_of_scope
  - utter_ask_continue
* affirm
  - user_form
  - form{"name":"user_form"}  
  - utter_slots_values
  - utter_complete_form

## no survey
* greet
  - utter_greet
* deny
  - utter_goodbye

## ask questions form
* greet
  - utter_greet
* affirm
  - user_form
  - form{"name":"user_form"}    
* ask_dietary_changes
  - utter_dietary_info
  - user_form
  - form{"name":"null"}  
  - utter_complete_form
<!-- 
## calorie form
* greet
  - utter_greet
* calorie_intake
  - calorie_form
  - form{"name":"calorie_form"}   
  - form{"name":"null"} 
  - utter_slots_values
  - utter_complete_form
* thankyou
  - utter_no_worries
  - utter_goodbye -->


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
- utter_dietary_info

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



