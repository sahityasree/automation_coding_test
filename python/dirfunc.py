"""when no parameters are passed Note that we have not imported any modules """
print(dir())
import math
import random
#after import statements
print(dir())
"""
 when a module Object is passed as parameter.import the random module Prints list which 
 contains names of attributes in random function """
print("The contents of random library are ::") 

print(dir(random)) 
li=[1,2,3]
dic={}
"""dir() will return all the available list methods in current local scope """
print(dir(li))
"""Call dir() with the dictionary name "d" as parameter. Return all the available dict methods in the  
current local scope """
print(dir(dic))

class School: 
    def __dir__(self): 
        return['physics', '200', 
               'chemistry', '100', 'date'] 

my_obj = School() 
"""Python3 program to demonstrate working of dir(), when user defined objects are passed 
are parameters. Creation of a simple class with __dir()__ method to demonstrate it's working """
print(dir(my_obj)) 

