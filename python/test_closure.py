
"""
->Closures can avoid the use of global values and provides some form of data hiding. 
->It can also provide an object oriented solution to the problem.
->When there are few methods (one method in most cases) to be implemented in a class,
 closures can provide an alternate and more elegant solutions. But when the number of attributes and methods get larger, better implement a class.
->Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.

"""


def outer_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier
    
def test_closure():
    times3 = outer_multiplier_of(2) #Closure function by calling outer_multiplier_of()
    times5 = outer_multiplier_of(4) #Closure function by calling outer_multiplier_of()
    print(times3(9)) #calling closure function which actually calls multiplier()
    print(times5(3))
    print(times5(times3(2)))

test_closure()