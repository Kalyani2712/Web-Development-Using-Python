#Polymorphism :
class animal:
    def sound(self):
        print("animal sound")
class dog(animal):
    def sound(self):
        print("dog sound")
class cat(animal):
    def sound(self):
        print("cat sound")
class lion(animal):
    def sound(self):
        print("lion sound")
        
a=animal()
a.sound()
d=dog()
d.sound()
c=cat()
c.sound()
l=lion()
l.sound()

#Output:
# animal sound
# dog sound
# cat sound
# lion sound    

#In the above example, we have created a class animal and three classes dog, cat, and lion which are inherited from the animal class.   
#All the classes have a method sound() which prints the sound of the animal.
#When we create an object of the animal class and call the sound() method, it prints animal sound.


#Operator Overloading:

class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self.x+other.x,self.y+other.y
a=A(10,20)
b=A(30,40)
print(a+b)
