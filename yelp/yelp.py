from dotenv import load_dotenv
from queries import search_query
import os
import requests
import json

load_dotenv()

api_key = os.getenv('API_KEY')

header = {
  'Authorization': f'bearer {api_key}', 
  'Content-Type':"application/json"
}
url='https://api.yelp.com/v3/graphql'

response = requests.post(url, json={'query': search_query}, headers=header)
businesses = response.json()['data']['search']['business']

results = json.dumps(businesses, indent=2)

with open('results.json', 'w') as file:
  file.write(results)