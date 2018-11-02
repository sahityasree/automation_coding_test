
"""checking object is passed to help() (not a string)"""
help(list)
help(dict)
help(print)
help([1,2])
"""string is passed as an argument to help()"""
help('random thing')
help('print')
help('def')
help('math.pow')

"""no argument is passed to help()"""
#help()

"""__import()__:
In general, pow() is a method defined in math module. 
You can call this function using the following syntax: math.pow
However, using __import__() changed the way to access fabs()"""

mathematics = __import__('math', globals(), locals(), [], 0)

print(mathematics.pow(2,5))
