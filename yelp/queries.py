search_query = '''
query GetResults($amount: Int, $term: String, $location: String)
{
  search(term: $term,
          location: $location,
          limit: $amount
          sort_by: "distance") {
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
