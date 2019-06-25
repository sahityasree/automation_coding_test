import mysql.connector
"""Connection of mysql from  and creating tables and fileds
"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="mydatabase1"
 
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase1")
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("show tables")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "was inserted.")
print("hi")
