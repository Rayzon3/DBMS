#Pract-1
import sqlite3

conn = sqlite3.connect('Shop.db') #connecting to db
c = conn.cursor() #creating cursor object
#creating table Shop_items
c.execute(''' CREATE TABLE Shop_items
                            (Item text, Symbol text, Expiry text, Quatity real, MRP real)''')
#inserting a row of data
c.execute("INSERT INTO Shop_items VALUES ('Rice', 'RCE', '2020-8-23', 10 ,100)")
conn.commit()

c.execute("INSERT INTO Shop_items VALUES ('Wheat', 'WHT', '2020-7-23', 5, 70)")
c.execute("INSERT INTO Shop_items VALUES ('Apples', 'APL', '2020-7-43', 5, 80)")
c.execute("INSERT INTO Shop_items VALUES ('Soap', 'SOP', '2020-9-23', 0.120, 40)")
conn.commit()

#printing
for row in c.execute('SELECT * FROM Shop_items'):
  print(row)
