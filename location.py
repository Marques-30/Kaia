import requests
import os
from dotenv import load_dotenv


load_dotenv()

URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ") #taking user input
api_key =  os.getenv('GEOCODE_AIP_KEY') # Acquire from developer.here.com
PARAMS = {'apikey':api_key,'q':location} 

# sending get request and saving the response as response object 
r = requests.get(url=URL, params=PARAMS) 
data = r.json()

latitude = data['items'][0]['position']['lat']
longitude = data['items'][0]['position']['lng']

print(f'{str(latitude)}, {str(longitude)}')