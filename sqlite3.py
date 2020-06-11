import sqlite3

# create new database
conn = sqlite3.connect('Demo_table.db')

# create Cursor to execute queries
cur = conn.cursor()

print('Databse created.')

# save changes
conn.commit()
print('Changes saved.')

# close database connection
conn.close()
print('Connection closed.')

# connect to existing database
conn = sqlite3.connect('Demo_table.db')
cur = conn.cursor()

# create table in database
cur.execute('CREATE TABLE CUSTOMER( User_ID INTEGER PRIMARY KEY NOT NULL,Product_ID INTEGER NOT NULL, Name TEXT NOT NULL, Gender TEXT NOT NULL, AGE INTEGER NOT NULL,  CITY TEXT); ')

# commit and save changes to database
conn.commit()

cur.execute('''Insert Into Customer ('User_ID','Product_ID','Name','Gender','AGE','CITY') Values (1006, 3, 'Princess Diana', 'Female', 28, 'Amazons');''')
# Execute multiple commands at once
cur.executescript('''Insert Into CUSTOMER Values(1005, 3, 'Clark Kent', 'Male', 36, 'Metropolis');  Insert Into CUSTOMER Values(1003, 4, 'Bruce Wayne', 'Male', 39, 'Gotham City');  ''')

# Insert maultiple values into table at once
customers = [(1004, 2, 'John Wick', 'Male', 32, 'New York'),(1001, 1, 'Tony Stark', 'Male', 35, 'New York'),(1002, 3, 'Gordon Ramsey', 'Male', 38, 'London') ] 
cur.executemany('Insert Into CUSTOMER Values (?,?,?,?,?,?)', customers)
conn.commit()
# Fetch all rows of query result
cur.execute('SELECT * FROM CUSTOMER;').fetchone()

# iterate over the rows 
for row in cur.execute('SELECT Name FROM CUSTOMER;'):
    print(row)

# Fetch all rows of query result which returns a list
cur.execute('SELECT * FROM CUSTOMER;').fetchall()

for row in cur.execute('SELECT * FROM CUSTOMER;'):
    print(row)

