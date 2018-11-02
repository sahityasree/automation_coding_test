import math
import random

def Numbers():
    print ("the absolute value is -45: ", abs(-45))
    print("the largest number is :", max(-20, 100, 400))
    print("the smallest number is :", min(-80, -20, -10))
    print("the power value is :",math.pow(100, 2))
    print("the power value is :",math.sqrt(100))
    print ("returns a random number from range(100) : ",random.choice(range(100)))
    print ("random number : ", random.random())
    list = [20, 16, 10, 5];
    random.shuffle(list)
    print("the shuffle of list is ",list)
    
def Strings():
    var1 = 'Hello World!'
    var2 = "Python Programming"
    var3= "Hello"
    print ("var1[0]: ", var1[0])
    print ("var2[1:5]: ", var2[1:5])
    print("the string concatination:",var1+var2)
    print("the repetition of string is:",var1*2)
    print ("the find function is :",var1.find(var3))
    print("the index function is :",var1.index(var3))
    print("the strislower function is:",var1.islower())
    print("the isspace() function is:",var1.isspace())
    print("the strip() function is:",var1.strip( '*' ))
    print ("the zfill() function is  : ",var1.zfill(40))
    
def Lists():
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [10, 20, 3, 24, 56, 16, 70 ]
    list1[2] = 2001
    print("New value available at index 2 : ", list1[2])
    del list1[2]
    print("New list after deleting index 2 : ", list1)
    print("the reverse slice ",list1[-2])
    print("the slice operations : ",list1[1:])
    print("the slice operations : ",list2[1:3])
    print("the length of list is:",len(list1))
    print("the concatination of lists is:",list1+list2)
    print("the repetition of lists is:",list1*2)
    print("the max of list is:",max(list2))
    print("the min of list is:",min(list2))
    t=(1,2,3) 
    print("convert tuple to list:",list(t))
    list1.append(1998)
    print(list1)
    print("the index of physics is:",list1.index('physics'))
    list1.pop(-1)
    print("after poping the item",list1)
    list1.remove('physics')
    list1.reverse()
    print("the reverse is:",list1)
    list2.sort()
    print("the sorting order is:",list2)
    
def Tuples():
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (10, 2, 13, 40, 25 )
    print ("tup1[0]: ", tup1[0])
    print ("tup2[1:5]: ", tup2[1:5])
    tup3=tup1+tup2
    print("the concatination is:",tup1+tup2)
    print("the repetition is:",tup1*2)
    print("the slicing is:",tup1[1:])
    print("the slicing is:",tup1[1:3])
    print("the slicing is:",tup1[-2])
    del tup3
    print("length of tuple is:" ,len(tup1))
    print("length of tuple is:" ,max(tup2))
    print("length of tuple is:" ,min(tup2))
    li=[1,23,3]
    print("the conversion of list to tuple",tuple(li))

def Dicts():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print ("dict['Name']: ", dict['Name'])
    print ("dict['Age']: ", dict['Age'])
    dict['School'] = "DPS School"
    print("after updating:",dict['School'])
    print("the length of dictionary is:",len(dict))
    print("the string reprentation of dictionary is:",str(dict))
    print("the type of variable is:",type(dict))
    dict2 = dict.copy()
    print("the copy operator is",dict2)
    print("the items are",dict.items())
    print("the keys are:",dict.keys() )
    print("the values are:",dict.values())
    dict1 = {'Sex': 'female' }
    dict.update(dict1)
    print("the values after update",dict)
    del dict['Name']
    print("after removing ",dict)
Dicts()   
    
    



