## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## uncertain path 1
* ident_inquiry
  - utter_intro
* personal_inquiry
  - utter_hobby
- book_recommend_form
- form{"name": "book_recommend_form"}
* inform_books
  - utter_ask_number
* enter_phone_number
  - action_search_books
  - action_recommend
  - form{"name": null}
* goodbye
  - utter_thanks

## say goodbye
* goodbye
  - utter_goodbye

## primary books path
* greet
  - utter_greet
  - utter_hobby
* agree
  - utter_ask
  - book_recommend_form
  - form{"name": "book_recommend_form"}
* inform_books
  - utter_ask_number
* enter_phone_number
  - action_search_books
  - action_recommend
  - form{"name": null}
* goodbye
  - utter_thanks

## books
* greet
  - utter_greet
  - utter_hobby
* agree
  - utter_ask
  - book_recommend_form
  - form{"name": "book_recommend_form"}
* inform_books
  - utter_ask_number
* enter_phone_number
  - action_search_books
  - action_recommend
  - form{"name": null}

## recommend book path
* greet
  - utter_greet
  - utter_intro
* personal_inquiry
  - utter_hobby
* agree
  - utter_ask
- book_recommend_form
- form{"name": "book_recommend_form"}
* inform_books
  - utter_ask_number
* enter_phone_number
  - action_search_books
  - action_recommend
  - form{"name": null}
* goodbye
  - utter_thanks

## talk about books
* greet
  - utter_intro
  - utter_hobby
* agree
  - utter_ask
  - book_recommend_form
  - form{"name": "book_recommend_form"}
* inform_books
  - utter_ask_number
* enter_phone_number
  - action_search_books
  - action_recommend
  - form{"name": null}
* goodbye
  - utter_thanks

## incorrect book path
  - form{"name": "book_recommend_form"}
  - utter_ask
  * inform_books
  - utter_ask_number
* enter_phone_number
  - action_recommend

## dislike books path
* greet
  - utter_greet
  - utter_intro
  - utter_hobby
* deny
  - utter_disappoint

## New Story

* greet
    - utter_intro
    - utter_hobby
* agree
    - utter_ask
    - book_recommend_form
    - slot{"requested_slot":"genre"}
* inform_books{"genre":"scifi"}
    - utter_ask_number
    - book_recommend_form
    - slot{"requested_slot":"genre"}
* enter_phone_number{"phone_number":"15105906785"}
    - action_search_books
    - action_recommend
    - action_deactivate_form
    - slot{"requested_slot":null}
    - utter_thanks
