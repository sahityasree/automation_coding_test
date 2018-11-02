"""

Fixures leverage a concept of dependancy injection
"""
import pytest
import mysql.connector
#from fixtures.test_tfixures import mysql

@pytest.fixture(scope="module")
def conn():
    print("setting up connection")
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="mydatabase")
    mycursor = mydb.cursor()
    yield mycursor #executed and connected only once
    
    mydb.close()
    mycursor.close()
    print(" closing DB")
    
      
def test_William_id(conn):
    conn.execute("select id from customers where name='William'")
    result=conn.fetchall()
    for x in result:
        print(x)
        
def test_Ben_addr(conn):
    conn.execute("select address from customers where name='Ben'")
    result=conn.fetchall()
    for x in result:
        print(x)
    
    
