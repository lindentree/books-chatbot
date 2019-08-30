# This files contains your custom actions which can be used to run
# custom Python code.
#
import sys
import requests
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
sid = os.getenv('SID')
auth_token = os.getenv('TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
from twilio.rest import Client

client = Client(sid, auth_token)

# See this guide on how to implement these actions:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
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
#         dispatcher.utter_message("Hello World!")
#
#         return []

class BookSearchForm(FormAction):

    def name(self):
        return "book_recommend_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["genre", "phone_number"]

    def submit(self, dispatcher, tracker, domain):
        """Define what the form has to do
              after all required slots are filled"""
        dispatcher.utter_template('utter_submit', tracker)
        return []

class ActionSearchBooks(Action):
    def name(self):
        return "action_search_books"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for books")
        
        book_genre = tracker.get_slot("genre")
        url = "https://www.googleapis.com/books/v1/volumes?q=subject:" + book_genre
       
        r = requests.get(url)
        data = r.json()

        parsed = [k for k in data['items'] if k['volumeInfo']['previewLink']]
        link = parsed[0]['volumeInfo']['previewLink']#implement better recommendation sorting later
        return [SlotSet("recommendations", link)]


class ActionRecommend(Action):
    def name(self):
        return "action_recommend"

    def run(self, dispatcher, tracker, domain):
        user_number = tracker.get_slot("phone_number")  
        test = tracker.get_slot("recommendations")

        if user_number is None: 
            dispatcher.utter_message("Sorry, didn't get a valid number")
            return []

        elif test is None:
            dispatcher.utter_message("Sorry, didn't find anything")
            return []
        else:

            user_number = "+" + user_number

            placeholder = "http://books.google.com/books?id=CXvurQEACAAJ&hl=&source=gbs_api"

            message = client.messages.create(
                to= user_number, 
                from_=twilio_number,
                body=test)

            #print(message.sid)
            dispatcher.utter_message("did you get my recommendation?")
            return []
