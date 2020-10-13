import pyttsx3
import requests, json
import os
import sys
import time
import datetime
import smtplib, ssl

def emailSend(send, sub):
  port = 587  # For starttls
  smtp_server = "smtp.gmail.com"
  password = ""
  kaia_email = ""
  sender_email = input("Please enter your email: ")
  Text = send
  Subject = sub
  message = 'Subject: {}\n\n{}'.format(Subject, Text)
  context = ssl.create_default_context()
  with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(kaia_email, password)
      server.sendmail(kaia_email, sender_email, message)

def timer(engine):
	engine.say('What date is your flight: ')
	engine.runAndWait()
	flight = input("What date is your flight: ")
	engine.say("what time is your flight: ")
	engine.runAndWait()
	time = input("what time is your flight: ")
	month = flight.split("/")[0]
	day = flight.split("/")[1]
	year = flight.split("/")[2]
	hour = time.split(":")[0]
	minute = time.split(":")[1]
	present = datetime.datetime.now()
	future = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), 00)
	difference = future - present
	print(difference)
	engine.say('Your flight is in ' + str(difference))
	engine.runAndWait()
	engine.say("Would you like to be email or texted updates on this?")
	engine.runAndWait()
	email = input("Would you like to be email or texted updates on this? ")
	if email.lower() == "email":
		send = 'Your flight is in ' + str(difference)
		sub = "Kaia report on Flight time"
		emailSend(send)
	elif email.lower() == "texted":
		text()

def google():
	# enter your api key here 
	api_key = 'Your_API_key'
	# url variable store url 
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
	# The text string on which to search 
	query = input('Search query: ') 
	# get method of requests module 
	# return response object 
	r = requests.get(url + 'query=' + query +
	                        '&key=' + api_key) 
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
engine.say('Hello ' + user)
engine.runAndWait()
engine.say('How can I help you today? ')
engine.runAndWait()
engine.say("Please pick one of the following choices: Flight, Hotel, Restaurant, or Bar")
engine.runAndWait()
choice = input("Please pick one of the following choices: \n Flight \n Hotel \n Restaurant \n Bar \n")
if choice.lower() == 'flight':
	timer(engine)
elif choice.lower() == 'hotel':
	hotel()
	email = input("Would you like to be email updates on this?")
elif choice.lower() == 'bar':
	bar()
	email = input("Would you like to be email updates on this?")
else:
	Restaurant()
	email = input("Would you like to be email updates on this?")

