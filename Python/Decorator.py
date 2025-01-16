'''decorator is a function that takes another function as an argument and add some functionality to it and returns a new function.
a decorator is a function that takes another function as an argument and returns a new function


#Decorators are used to add new functionality to an existing function without modifying its source code.
#Decorators are a way to extend the functionality of a function without modifying its source code.

syntax :

@decorator_name
def function_name():
    #code

def decorator_name(function):
    def wrapper():
        #code
        function()
        #code
    return wrapper


''' 

# def greet_decorator(func):
#     def wrapper(): 
#         print("Good Morning")
#         func()
#         print("Good Night")
#     return wrapper

# @greet_decorator  
# def name_print():
   
#     print("My name is kalyani")
   
# name_print()



# def argument_decorator(func):
#     def wrapper( *args, **kwargs):
#         print(f"arguments :" , *args, **kwargs)
#         return  func( *args, **kwargs)
#     return wrapper
# @argument_decorator
# def add(x,y):
#     return x+y
# result=add(10,20)
# print(result) 


# create 2 decorator having same functionality:


# def decorator1(func):
#     def wrapper():
#         print("decorator1")
#         func()  
#         print("decorator2")  
#     return wrapper  

# def decorator2(func):    
#     def wrapper():
#         print("decorator3 ")
#         func()   
#         print("decorator4") 
#     return wrapper 

# @decorator1
# @decorator2
# def name_print():
#     print("My name is kalyani 5")  
# name_print()


#Advanced Decorators :
# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat(3)
# def greet(name):
#     print(f"Hello {name}")

# greet("Kalyani") 


#Create a decorator whis show how much time it takes to execute the function:


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time : .4f} seconds to execute.")
        return result
    return wrapper  

@timer
def my_function():
    time.sleep(5)

my_function()
