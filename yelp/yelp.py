from dotenv import load_dotenv
from .queries import search_query
import os
import requests
import json

load_dotenv()


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


def search_restaurant(engine, choice):
    api_key = os.getenv('YELP_API_KEY')

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
        'price': "1,2,3,4"
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

    with open('results.json', 'w') as file:
        engine.say(f'Writing to {file.name}')
        engine.runAndWait()
        file.write(results)
