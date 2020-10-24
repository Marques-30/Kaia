search_query = '''
{
  search(term: "burrito",
          location: "670 natoma, san francisco",
          limit: 5
          price: "1") {
            total
            business {
              name
              id
              alias
              phone
              display_phone
              price
              distance
              location {
                address1
                city
              }
              coordinates {
                latitude
                longitude
              }
            }
          }
}
'''