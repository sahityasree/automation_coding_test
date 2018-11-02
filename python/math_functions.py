class math1:
    def __init__(self):
        print ("Calling parent constructor1")
    def add(self,a,b):
        c=a+b
        print("addition is :",c)
        
    def diff(self,a,b):
        c=a-b
        print("diffrence is :",c)
        
class math2:   
    def __init__(self):
        print ("Calling parent constructor2")
    def mul(self,a,b):
        c=a*b
        print("multiplication is :",c)
        
    def div(self,a,b):
        if(b!=0):
            c=a/b
            print("division is :",c)
        else:
            print("divide by zero error")
        
    
class math(math1,math2):
    def __init__(self):
        print ("Calling child constructor")
    def setvalue(self,a):
        self.a=a
        print("set value is", a)
            
m = math()
m.setvalue(5)
m.add(2,3)
m.diff(10,2)
m.mul(5,2)
m.div(8,2)