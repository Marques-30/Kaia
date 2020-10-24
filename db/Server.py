import sqlite3

conn = sqlite3.connect('User_location.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
c.execute('''CREATE TABLE CLIENTS
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [phone] integer, [email] text)''')
          
# Create table - Flight
c.execute('''CREATE TABLE Flights
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Date_Time_Flight] text)''')
        
#Create table - Location
c.execute('''CREATE TABLE Location
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Location] text)''')
                 
conn.commit()