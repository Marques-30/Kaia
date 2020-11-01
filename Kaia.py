import pyttsx3
import requests
import json
import os
import sys
import time
import datetime
import smtplib
import ssl
import sqlite3
from twilio.rest import Client
from .queries import search_query
import json

def get_query_variables(engine):
    engine.say('What is your current location?')
    engine.runAndWait()
    location = input('What is your current location(address, city)? ')
    engine.say('How many results do you want?')
    engine.runAndWait()
    amount = input('How many results do you want? ')
    engine.say('Would you like to see only cheap results?')
    engine.runAndWait()
    cheap = input('Would you like to see only cheap results?')

    if cheap.lower() == 'yes':
        cheap_results = True
    else:
        cheap_results = False

    return location, int(amount), cheap_results

def search(engine, choice, c, conn):
    api_key = os.getenv('iCkiw4en2tSbbxzHRJQiMra8x3p47h_1AEkPx5r6gdDEYxxjPDa6rvXOT0xL2BTN8qLTIH34_O-rJZRSiO63DAdvEvD9UBtyGaczIBqOF4K4F0UCc6-Qg561byeFX3Yx')

    header = {
        'Authorization': f'bearer {api_key}',
        'Content-Type': "application/json"
    }
    url = 'https://api.yelp.com/v3/graphql'
    location, amount, cheap_results = get_query_variables(engine)

    variables = {
        'term': choice,
        'location': location,
        'amount': amount,
        'price': "1,2,3,4",
        'rating': "1,2,3,4,5",
        'hours': ""
    }
    if cheap_results:
        variables['price'] = "1"
    search = {
        'query': search_query,
        'variables': variables
    }
    response = requests.post(url, json=search, headers=header)
    businesses = response.json()['data']['search']['business']

    results = json.dumps(businesses, indent=2)
    print(results)

    with open('results.json', 'w') as file:
        engine.say(f'Writing to {file.name}')
        engine.runAndWait()
        file.write(results)
    engine.say("Would you like to be email or texted updates on this?")
    engine.runAndWait()
    email = input("Would you like to be email or texted updates on this? ")
    if email.lower() == "email":
        send = f'Your flight is in {difference} moments to {location}'
        subject1 = "Kaia report on Flight time"
        emailSend(send, engine, subject1)
    elif email.lower() == "texted":
        send = f'Your flight is in {difference} moments to {location}'
        text(engine, user, send)
    else:
        print("Thank you")

def text(engine, user, send, c, conn):
    # Your Account SID from twilio.com/console
    account_sid = os.getenv('ACea4b3bbf0e980bf3f436886e8ab16273')
    # Your Auth Token from twilio.com/console
    auth_token = os.getenv('933d2d7c29e953c54ae45bdb11415048')
    Phone_Text = input("Please enter your phone number to text: ")
    engine.say("Please enter your phone number to text: ")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+1" + Phone_Text,
        from_="+17029963546",
        body="Hello " + user + ",\n" + send)
    c.execute('''UPDATE TABLE CLIENTS
        ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [phone] integer, [email] text)''')
    conn.commit()

def nightlife(engine, ploc, c, conn):
    api_key = os.getenv('iCkiw4en2tSbbxzHRJQiMra8x3p47h_1AEkPx5r6gdDEYxxjPDa6rvXOT0xL2BTN8qLTIH34_O-rJZRSiO63DAdvEvD9UBtyGaczIBqOF4K4F0UCc6-Qg561byeFX3Yx')

    header = {
        'Authorization': f'bearer {api_key}',
        'Content-Type': "application/json"
    }
    url = 'https://api.yelp.com/v3/graphql'
    location, amount, cheap_results = get_query_variables(engine)

    variables = {
        'term': "events",
        'location': location,
        'amount': amount,
        'price': "1,2,3,4",
        'rating': "1,2,3,4,5",
        'hours': hours
    }
    if cheap_results:
        variables['price'] = "1"
    search = {
        'query': search_query,
        'variables': variables
    }
    response = requests.post(url, json=search, headers=header)
    businesses = response.json()['data']['search']['business']

    results = json.dumps(businesses, indent=2)
    print(results)

    with open('results.json', 'w') as file:
        engine.say(f'Writing to {file.name}')
        engine.runAndWait()
        file.write(results)
    engine.say("Would you like to be email or texted updates on this?")
    engine.runAndWait()
    email = input("Would you like to be email or texted updates on this? ")
    if email.lower() == "email":
        send = f'Your flight is in {difference} moments to {location}'
        subject1 = "Kaia report on Flight time"
        emailSend(send, engine, subject1)
    elif email.lower() == "texted":
        send = f'Your flight is in {difference} moments to {location}'
        text(engine, user, send)
    else:
        print("Thank you")


def location(engine):
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    location = input("What is your current location(address, city)? ")  # taking user input
    engine.say("What is your current location(address, city)?")
    api_key = os.getenv('HMAroqS9GA6WZo1y67NBFGvX_LcB9JdUJs3MuVyWc4U')  # Acquire from developer.here.com
    PARAMS = {'apikey': api_key, 'q': location}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    print(f'{str(longitude)}, {str(latitude)}')
    ploc = str(longitude) + "," + str(latitude)

def emailSend(send, subject1, engine):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    password = os.getenv('itkdwagifslfdxma')
    kaia_email = os.getenv('kaiaassistant39@gmail.com')
    sender_email = input("Please enter your email: ")
    Text = send
    Subject = str(subject1)
    message = f'Subject: {Subject}\n\n{Text}'
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(kaia_email, password)
        server.sendmail(kaia_email, sender_email, message)
        engine.say("An email has been sent out please wait about 5 minutes for it to show in your inbox.")


def timer(engine, user, c, conn):
    engine.say('What date is your flight: ')
    engine.runAndWait()
    flight = input("What date is your flight: ")
    engine.say("what time is your flight: ")
    engine.runAndWait()
    time = input("what time is your flight: ")
    engine.say("Where are you heading to? ")
    location = input("Where are you heading to? ")
    month = flight.split("/")[0]
    day = flight.split("/")[1]
    year = flight.split("/")[2]
    hour = time.split(":")[0]
    minute = time.split(":")[1]
    present = datetime.datetime.now()
    future = datetime.datetime(int(year), int(
        month), int(day), int(hour), int(minute), 00)
    difference = future - present
    print(difference)
    engine.say(f'Your flight is in {difference} moments to {location}')
    engine.runAndWait()
    engine.say("Would you like to be email or texted updates on this?")
    engine.runAndWait()
    email = input("Would you like to be email or texted updates on this? ")
    if email.lower() == "email":
        send = f'Your flight is in {difference} moments to {location}'
        subject1 = "Kaia report on Flight time"
        emailSend(send, engine, subject1, c)
    elif email.lower() == "text":
        send = f'Your flight is in {difference} moments to {location}'
        text(engine, user, send, c)
    else:
        print("Thank you")

def google():
    # enter your api key here
    api_key = 'Your_API_key'
    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    # The text string on which to search
    query = input('Search query: ')
    # get method of requests module
    # return response object
    r = requests.get(f'{url}query={query}&key={api_key}')
    # json method of response object convert
    #  json format data into python format data
    x = r.json()
    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']
    # keep looping upto length of y
    for i in range(len(y)):
        # Print value corresponding to the
        # 'name' key at the ith index of y
        print(y[i]['name'])

conn = sqlite3.connect('Kaia_brain.db')
c = conn.cursor()
user = input("Hello what is your name: ")
language = input("What is your preferred language: ")
if language.lower() == "spanish":
    voice_name = u'Juan'
    voice_language = u'es_MX'
elif language.lower() == "japanese":
    voice_name = u'Kyoko'
    voice_language = u'ja_JP'
elif language.lower() == "chinese":
    voice_name = u'Zuzana'
    voice_language = u'cs_CZ'
elif language.lower() == "indian":
    voice_name = u'Lekha'
    voice_language = u'hi_IN'
else:
    voice_name = u'Samantha'
    voice_language = u'en_US'
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if voice.name == voice_name and voice.languages[0] == voice_language:
        engine.setProperty('voice', voice.id)
        break
engine.runAndWait()
engine.say(f'Hello {user}')
engine.runAndWait()
engine.say('How can I help you today?')
engine.runAndWait()
location(engine)
engine.say(
    "Please pick one of the following choices: Flight, Hotel, Restaurant, or Bar")
engine.runAndWait()
choice = input(
    "Please pick one of the following choices: \n* Flight \n* Hotel \n* Restaurant \n* Bar \n* Night life \n")
if choice.lower() == 'flight':
    timer(engine, user, c, conn)
elif choice.lower() == 'hotel':
    search(engine, choice, c, conn)
elif choice.lower() == 'bar':
    search(engine, choice, c, conn)
elif choice.lower() == 'restaurant':
    search(engine, choice, c, conn)
else:
    nightlife(engine, c)