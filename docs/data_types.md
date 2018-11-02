##Data Types in Python##
**Ref python program:** datatypes.py

Python has five standard data types:

-	Numbers
-	String
-	List
-	Tuple
-	Dictionary

### Numbers ###
Number data types store numeric values.  Integers, floating point numbers and complex numbers falls under Python numbers category. They are defined as int, float and complex class in Python. Number objects are created when you assign a value to them. 

For example:-

- var1 = 1 --integer
- var2=2.0    ---floating point number
- var3=1+2j    ----complex number

You can also delete the reference to a number object by using the del statement. The syntax of the del statement is

- del  var1[,var2]
- del  var1
- del  var1.var2

There are several mathematical functions  used in numbers data type they are abs,ceil,floor, exp,cmp, fabs, log,log10, max, min, modf, pow, round, sqrt.  These all imported from math module in python. The mainly used functions are described below.

**abs():**  The abs() method returns the absolute value of x i.e. the positive distance between x and zero. 

**Syntax:** abs ( x ) where x is a numeric expression. 

**max():**  The max() method returns the largest of its arguments i.e. the value closest to positive infinity.

**Syntax:** max(x,y,z...) where x,y,z are the numbers 

**min():**The method min() returns the smallest of its arguments i.e. the value closest to negative infinity.

**Syntax:** min(x,y)  where x is numeric value

**pow():**  pow() function is used the find the power value. This function was imported from math module.

**Syntax:**  pow(x,y) where x,y are numeric values 

**sqrt():**
The sqrt() method returns the square root of x for x > 0. This function was also imported from math module.

**Syntax:** import math math.sqrt( x )

**Random Number Functions :**

Random numbers are used for games, simulations, testing, security, and privacy applications. Python includes the following functions that are commonly used.

**choice():**
The choice() method returns a random item from a list, tuple, or string. 

**Syntax:** methodchoice(seq).

**Note:** This function is not accessible directly, so we need to import the random module and then we need to call this function using the random static object.

**randrange():**
The randrange() method returns a randomly selected element from range(start, stop, step). 

**Syntax:**randrange ([start,] stop [,step])

**Note:** This function is not accessible directly, so we need to import the random module and then we need to call this function using the random static object.
randomly select a number between 0-99

**random():**
The random() method returns a random floating point number in the range [0.0, 1.0].
**Syntax:** random ( )

**Note:** This function is not accessible directly, so we need to import the random module and then we need to call this function using the random static object.

**shuffle():**
The shuffle() method randomizes the items of a list in place.

**Syntax :**shuffle (lst,[random]) 
###Strings###
Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes. Python treats single quotes the same as double quotes. Creating strings is as simple as assigning a value to a variable.
For example:-

- var1 = 'Hello World!' 
- var2 = "Python Programming"

**Accessing Values in Strings :**
Python does not support a character type; these are treated as strings of length one, thus also considered a sub string.To access sub strings, use the square brackets for slicing along with the index or indices to obtain your sub string.

**Updating Strings :**
You can "update" an existing string by (re)assigning a variable to another string. The new value can be related to its previous value or to a completely different string altogether. 

**find():** 
The find() method determines if the string str occurs in string, or in a sub string of string if the starting index beg and ending index end are given. 

**Syntax:** str.find(str, beg=0 end=len(string))

**index():**
The index() method determines if the string str occurs in string or in a substring of string, if the starting index beg and ending index end are given. This method is same as find(), but raises an exception if sub is not found. 

**Syntax:** str.index(str, beg=0 end=len(string))

**islower():**
The islower() method checks whether all the case-based characters (letters) of the string are lowercase. 

**Syntax :** str.islower()

**join():**

The join() method returns a string in which the string elements of sequence have been joined by str separator.

**Syntax :** str.join(sequence)

**len():**
The len() method returns the length of the string.

**Syntax:** len(str)

**replace():**

The replace() method returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.

**Syntax :** str.replace(old, new[, max])

**rfind():**

The rfind() method returns the last index where the substring str is found, or -1 if no such index exists, optionally restricting the search to string[beg:end].

**Syntax :** rfind(str, beg=0 end=len(string))

###Lists###

The list is the most versatile data type available in Python, which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that the items in a list need not be of the same type.Creating a list is as simple as putting different comma-separated values between square brackets. For example :

- list1 = ['physics', 'chemistry', 1997, 2000];
- list2 = [1, 2, 3, 4, 5 ];
- list3 = ["a", "b", "c", "d"];
 
accessing lists as same as strings.

- list1[1]=chemistry
- list2[-1]=5
- list1[1:]= 'chemistry', 1997, 2000

**len():** len() method returns the number of elements in the list.

**Syntax :** len(list) 

**max():**The max() method returns the elements from the list with maximum value.

**Syntax :** max(list)

**min():**The method min() returns the elements from the list with minimum value.

**Syntax :** min(list)

**list():** The list() method takes sequence types and converts them to lists. This is used to converta given tuple into list.

**Syntax:** list(seq )

**append():** The append() method appends a passed obj into the existing list.

**Syntax :**append(obj)

**index():**The index() method returns the lowest index in list that obj appears.

**Syntax :** index(obj)

**pop():** The pop() method removes and returns last object or obj from the list.

**Syntax :** pop(obj=list[-1])

**reverse():** The reverse() method reverses objects of list in place.

**Syntax :** reverse()

**sort():** The sort() method sorts objects of list, use compare function if given.

**Syntax :** sort([func]

###Tuple###
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The main difference between the tuples and the lists is that the tuples cannot be changed unlike lists. Tuples use parentheses, whereas lists use square brackets.Creating a tuple is as simple as putting different comma-separated values. Optionally, you can put these comma-separated values between parentheses also. 
For example

- tup1 = ('physics', 'chemistry', 1997, 2000)
- tup2 = (1, 2, 3, 4, 5 )
- tup3 = "a", "b", "c", "d"

The empty tuple is written as two parentheses containing nothing.

- tup1 = ();

To write a tuple containing a single value you have to include a comma, even though there is only one value.

- tup1 = (50,)

accessing tuple is same as list,strings. but tuples are non mutable.
 
**len():** The len() method returns the number of elements in the tuple.

**Syntax :** len(tuple)

**max():** The max() method returns the elements from the tuple with maximum value.

**Syntax :** max(tuple)

**min():** The min() method returns the elements from the tuple with minimum value.

**Syntax :** min(tuple)

**tuple():** The tuple() method converts a list of items into tuples.

**Syntax :** tuple(seq)
###Dictionary ###
Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.
Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

- dict={name:'sitha',age:20}
- dict[name]='sitha'

**len():** The method len() gives the total length of the dictionary. This would be equal to the number of items in the dictionary.

**Syntax :** len(dict)

**type():** The method type() returns the type of the passed variable. If passed variable is dictionary then it would return a dictionary type.

**Syntax :** type(dict)

**copy():** The method copy() returns a shallow copy of the dictionary.

**Syntax :** copy()

**get():** The method get() returns a value for the given key. If the key is not available then returns default value None.

**Syntax :** dict.get(key, default=None)

**items():** The method items() returns a list of dict's (key, value) tuple pairs.

**Syntax :** dict.items()

**keys():** The method keys() returns a list of all the available keys in the dictionary.

**Syntax :** dict.keys()

**update() :** The method update() adds dictionary dict2's key-values pairs in to dict. This function does not return anything.

**Syntax :** dict.update(dict2)

**values():**

The method values() returns a list of all the values available in a given dictionary.

**Syntax :** dict.values()








