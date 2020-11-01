import sqlite3

conn = sqlite3.connect('Kaia_brain.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
c.execute('''CREATE TABLE CLIENTS
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [phone] integer, [email] text)''')
          
# Create table - Flight
c.execute('''CREATE TABLE Flights
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Date_Time_Flight] text, [Flying_To] text, [Flying_From] text, [Connecting_Flight] text, [Time_of_Layover] text)''')
        
#Create table - Location
c.execute('''CREATE TABLE Restaurant
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Location] text, [Restaurant] text, [Price] integer, [Rating] integer)''')

#Create table - Bar                 
c.execute('''CREATE TABLE Bar
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Location] text, [Bar] text, [Price] integer, [Rating] integer)''')

#Create table - Hotel                 
c.execute('''CREATE TABLE Hotel
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Location] text, [Hotel] text, [Price] integer, [Rating] integer)''')

#Create table - Hotel                 
c.execute('''CREATE TABLE Nightlife
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Location] text, [Event] text, [Price] integer, [Rating] integer)''')

conn.commit()