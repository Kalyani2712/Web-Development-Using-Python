'''
Modules  are  files containing Python code that can include classes ,functions , variables , etc 
modules behefit :
1. Reusability
2. Modularity   
3. Encapsulation
'''  
import math
print(math.pi)
print(math.e)
print(math.sqrt(4))
print(math.pow(2,4))
print(math.log(10))
print(math.sin(90))


#create a class define one function and variable again and again create one class and use their functions
import math
class MyMath:
    def __init__(self):
        self.pi=3.14
        self.e=2.71
    def getPi(self):
        return self.pi
class MyMath2:
    def __init__(self):
        self.m=MyMath()
    def getPi(self):
        return self.m.getPi()
   
m=MyMath2()
print(m.getPi())




