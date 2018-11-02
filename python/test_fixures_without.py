import mysql.connector

def test_William_id1():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="mydatabase")
    mycursor = mydb.cursor()
    mycursor.execute("select id from customers where name='William'")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def test_Ben_addr1():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="mydatabase")
    mycursor = mydb.cursor()
    mycursor.execute("select address from customers where name='Ben'")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        
""" two issues in above code
-->Code repetetion
-->Creative expensive DB connection in every testcase
to fix the we use Fixtures
        
"""
