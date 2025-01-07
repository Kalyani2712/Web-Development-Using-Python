#Abstraction:

from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def do_something(self):
        pass
    
class AbstractChildClass(AbstractClass):
        print("This is a child class")

a= AbstractChildClass()
a.do_something()

#Output: This is a child class
# Cant instanciate an abstract class, but can inherit it.


#create a class name shape having abstract fuction area and perimeter and create a inheritance class rectangle (shape) and class circle (shape) and implement the area and perimeter function in both the classes.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

rectangle = Rectangle(5, 3)
print(rectangle.area())
print(rectangle.perimeter())

circle = Circle(5)
print(circle.area())
print(circle.perimeter())
