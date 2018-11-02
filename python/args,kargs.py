
"""
-->*args  are Non Keyword Arguments
--->*args is used to which allow us to pass the variable number of 
non keyword arguments to function.
--->In the function, we should use an asterisk * before the parameter name to pass 
variable length arguments.
--->The arguments are passed as a tuple and these passed arguments make tuple inside the function with same name as the parameter excluding asterisk *."""
def addition(*args):
    z = 0
    for num in args:
        z += num
    print(z)
"""
--->**kwargs are Keyword Arguments
--->It allows us to pass the variable length of keyword arguments to the function.
--->In the function, we use the double asterisk ** before the parameter name to denote 
this type of argument. 
--->The arguments are passed as a dictionary and these arguments make a dictionary 
inside function with name same as the parameter excluding double asterisk **.
"""
def printinfo( **inputdata):
     for key, value in inputdata.items(): #read items in dictionary
        print("{} is {}".format(key,value))
    

# Now you can call printinfo, addition function
addition(4, 5)#non keyword arguments
addition(2, 3, 4)
addition(3, 5, 10, 6)
printinfo( name="miki",age=50,  )# keyword arguments
printinfo( name="miki" ,sal=20000,age=20)

"""
-->*args passes variable number of non-keyworded arguments list and on which 
operation of the list can be performed.
--->**kwargs passes variable number of keyword arguments dictionary to function 
on which operation of a dictionary can be performed.
"""