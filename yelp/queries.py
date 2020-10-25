search_query = '''
query GetResults($amount: Int, $term: String, $location: String, $price: String)
{
  search(term: $term,
          location: $location,
          limit: $amount
          price: $price
          sort_by: "distance") {
            total
            business {
              name
              price
              location {
                address1
                city
              }
              hours {
                open {
                  day
                  start
                  end
                }
              }
              reviews {
                user {
                  name
                }
                rating
                text
              }
            }
          }
}
'''
