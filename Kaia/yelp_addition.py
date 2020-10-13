from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

Client_ID = "Yq3pDDuNQNUI-ManVtB09A"
api_key = "iCkiw4en2tSbbxzHRJQiMra8x3p47h_1AEkPx5r6gdDEYxxjPDa6rvXOT0xL2BTN8qLTIH34_O-rJZRSiO63DAdvEvD9UBtyGaczIBqOF4K4F0UCc6-Qg561byeFX3Yx"

# define our authentication process.
header = {'Authorization': 'bearer {}'.format(api_key),
          'Content-Type':"application/json"}

# Build the request framework
transport = RequestsHTTPTransport(url='https://api.yelp.com/v3/graphql', headers=header, use_json=True)

# Create the client
client = Client(transport=transport, fetch_schema_from_transport=True)
        
# define a simple query
query = gql('''
{
  business(id: "garaje-san-francisco") {
    name
    id
    is_claimed
    is_closed
    url
    phone
    display_phone
    review_count
    rating
    photos
  }
}
''')

# execute and print this query
print('-'*100)
print(client.execute(query))