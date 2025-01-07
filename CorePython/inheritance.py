
#if you want to run any code remove the comments and run the code.
#Inheritance
#Single Inheritance
# class Parent:
#     def speak(self):  
#         print("Parent speaking")

# class Child(Parent):
#     # pass
#     def eat(self):
#         print("Child eating")

# c = Child()
# c.speak()
# c.eat()

# Parent=Parent()
# Parent.speak()
# # Parent.eat()  # AttributeError: 'Parent' object has no attribute 'eat'

#Multiple Inheritance
# class Father:
#     def speak(self):
#         print("Father speaking")

# class Mother:
#     def eat(self):
#         print("Mother eating")

# class Child(Father, Mother):
#     # pass
#     def play(self):
#         print("Child playing")

# c = Child()
# c.speak()
# c.eat()
# c.play()

#MultiLevel Inheritance:

# class LivingBeing:
#     def breathe(self):
#         print("Living Being breathing")

# class Animal(LivingBeing):
#     def eat(self):
#         print("Animal Eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barking")


# d = Dog()
# d.breathe()
# d.eat()        
# d.bark()
# # d.eat()  # AttributeError: 'Dog' object has no attribute 'eat'


#Hierarchical Inheritance:
# class Parent:
#     def eat(self):
#         print("Parent eating")    

# class Child1(Parent):
#     def play(self):
#         print("Child1 playing")

# class Child2(Parent):
#     def study(self):
#         print("Child2 studying")

# c1 = Child1()
# c1.eat()
# c1.play()
# c2 = Child2()
# c2.eat()
# c2.study()


#Heirarchical Inheritance:

class Vehicle:
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def open_doors(self):
        print(" car: Opening  doors")

class Bike(Vehicle):
    def kick_start(self):
        print(" bike : Kick started")

c = Car()
c.start()
c.open_doors()
c.stop()

b = Bike()
b.start()
b.kick_start()
b.stop()


    






#self and super() in inheritance:
# class person:
#     def __init__(self,name):
#         self.name=name
        
#     def display(self):
#         print("Name:", self.name)
#         print("Color:", self.color)
     
#     def drive(self):
#         print("Vehicle is driving")
     
#     def stop(self):
#         print("Vehicle has stopped")
     
#     def turn(self):
#         print("Vehicle is turning")
     
# class Car(Vehicle):
#     def __init__(self, name, color, doors):
#         super().__init__(name, color)
#         self.doors = doors
     
#     def open_doors(self):
#         print("Opening", self.doors, "doors")
     
# class Bike(Vehicle):
#     def __init__(self, name, color, gears):
#         super().__init__(name, color)
#         self.gears = gears
     
#     def gear_shift(self):
#         print("Shifting gears to", self.gears)
#         print("Name:",self.name)

     
# class Employee(person):
#     def __init__(self,name,emp_id):
#        super().__init__(name)
#        self.emp_id=emp_id
#     def display(self):
#         print("Name:",self.name)
#         print(f"Emp_id: {self.emp_id}")

# e=Employee("kalyani",101)
# e.display()
