'''
Object oriented programming system  is a programming paradigm that provides a means of structuring 
programs so that properties and behaviors 
are bundled into individual objects. 

Class:
- A class is a blueprint or template that defines the properties (attributes) and 
behaviors (methods) of objects.

-Non Real world Entity


Object :

- An object is an instance of a class.

- When a class is defined, no memory is allocated 
but when it is instantiated (i.e. an object is created) memory is allocated.

- Real world Entity 

for example :
1.animal is a class and dog, cat, lion are object of that class.
2.vehicle is a class and car, bike, truck are object of that class.
3.furniture is a class and chair is an object of that class.
4.fruit is a class and apple mango , pineapple are an object

#syntax: 
object_name=class_name()
eg: 
car=vehicle()

constructor:
- A constructor is a special type of method (function) which is used to initialize the attribute of the object.
used on the time of object creation.

syntax:
def __init__(self):
    #code 
'''

#1.Class and Object :

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print(f"The {self.color} {self.brand} car is starting.")

#     def stop(self):
#         print(f"The {self.color} {self.brand} car has stopped.")

# my_car = Car("Toyota", "Red")
# my_car.start()
# my_car.stop()


#Constructor:
# class student:
#     def __init__(self):
#         print("constructor called")
# student();


# class student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# kalyani=student("kalyani", 90) #object creation
# print(kalyani.name)
# print(kalyani.marks)
# s2=student("s2", 80) #object creation
# print(s2.name)
# print(s2.marks)


'''
TYPES OF CONSTRUCTOR:
#1. Default constructor:
default constructor is the constructor which does not take any arguments.
syntax:
def __init__(self):
    #code
#2. Parameterized constructor
#3. Non-parameterized constructor
'''
# class car:
#     #attribute->class Property
#     wheels=4
#     def start_engine(self):
#         print("Engine is starting")

# C1=car()
# C1.start_engine()

# C2=car()
# C2.start_engine()


# class student:
#     college="CKT"
#     def __init__(self, name, age):
#         self.name = name #oject Attribute
#         self.age = age
# s1=student("kalyani", 22)
# print(s1.name, s1.age, s1.college)

# s2=student("s2", 23)
# print(s2.name, s2.age, s2.college)
 
       # create a studemt class and take name and marks of 5 subjcts as argument in constructor and print the total marks of student. completed : studentmarksAverage.py
       #Private attribute/method: example:privatedemo.py/
'''
       #Encapsulation: 
     
    #    bundling /binding
    #    wrapping up of data and methods into a single unit is called encapsulation.
    #   for example: class
            # data hiding
            achieve by using private attribute and methods

'

            
        #Abstraction: abstracrtion is a process of hiding the implementation details and showing only the functionality to the user.
        #Abstraction is achieved by using abstract class and interface.
        details are hidden
        #Abstract class:
        #An abstract class is a class that contains one or more abstract methods.
        #An abstract method is a method that is declared but not implemented.
       #syntax:
        Data Abstraction :
        class A:
            def show(self):
                pass
        class B(A):
            def show(self):
                print("showing")  
        b=B()
        b.show()
        #output: showing
        
       
       
       
       
       
       
       #Inheritance: 
       # inheritance is a mechanism in which one class acquires the property of another class.
       syntax:
       class parent:  //super class  
         //variables and methods
         class child(parent)://sub class
            //variables and methods
            
          #Types of inheritance:
          # Single inheritance:
        defination: when a class inherits only one class is called single inheritance.
        for eg :
        class A:
            pass
        class B(A):
            pass
            

          # Multiple inheritance:
            defination: when a class inherits multiple classes is called multiple inheritance.
            real life example:
            class father:
                pass
            class mother:
                pass
            class child(father, mother):
                pass
            -----------------------------------------------------
            for eg:
            class A:
                pass
            class B:
                pass            
            class C(A,B):
                pass
          # Multilevel inheritance: 
            defination: when a class inherits a class and that class inherits another class is called multilevel inheritance.
          # Hierarchical inheritance:
            defination: when multiple classes inherit a single class is called hierarchical inheritance.
          # Hybrid inheritance    :
           Hybrid inheritance is a combination of multiple and multilevel inheritance.  
                     #Polymorphism:
                                      #polymorphism means one name and multiple forms.
                                     #polymorphism achieve with overridding in python.
                                       #overloading and overriding
                                        #overloading:
                                      #overloading means defining multiple methods with the same name but different parameters.
                                      #overloading is not supported in python.
                                            #Method overloading:
                                            # Method overloading is the ability to define multiple methods with the same name but with different parameters.
                                            #Method overloading is not supported in python.
                                            #Sequence of parameters is not considered in python.
                                            acheive with same class
                                            # Constructor overloading is not supported in python.
                                            # Operator overloading is supported in python.
                                            # Operator overloading is the ability to define multiple methods with the same operator but with different parameters.
                                            # Operator overloading is achieved by defining a special method in the class.
                                            # The special method is called a magic method.
                                            # The magic method is defined with double underscores before and after the method name.
                                             # The magic method is called automatically when the operator is used.   
                                                               
                                      #overriding:
                                      #overriding means defining multiple methods with the same name and same parameters.
                                      #overriding is used in inheritance.
                                      #overriding is supported in python.
                                      #overriding is achieved with inheritance.
                                      class A:
                                          def show(self):
                                              print("A class")
                                      class B(A):
                                          def show(self):
                                              print("B class")
                                      b=B() 
                                      b.show()
                                      #output: B class

                                      
                                      #Self keyword:
                                      #self is a reference variable that refers to the current object.
                                      #self is used to access the attributes and methods of the class.
                                      

                        

'''
