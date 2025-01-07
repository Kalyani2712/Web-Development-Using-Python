'''
Exception Handling
defination: Exception handling is a mechanism
used to handle runtime errors so that normal flow of the program can be maintained.
abnormal termination of the program is avoided.
difference between error and exception:
error: 
error is a mistake in the program that is not handled.
    occurs by the user. at system level.
    programmer has not have control over the error.
eg , less ram , no internet connection, hardware failure etc. , less memory etc.
exception: 
exception is a runtime error that is handled.
            occurs by the program itself.
            we can handle exception by using try, except, finally and raise keywords.
            eg less memory, file not found, division by zero,type error etc.
'''
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# div=num1/num2
# print(div)
# print("End of the program")
#output: Enter first number:10 if we enter 0 then it will give error.

#ZeroDivisionError: division by zero
# num1=1
# num2=0
# div=num1/num2
# print(div)
# print("End of the program")

#TypeError: unsupported operand type(s) for /: 'int' and 'str'
# num1=int(input("Enter first number:"))
# num2=(input("Enter second number:"))
# div=num1/num2
# print(div)
# print("End of the program")

#Syntax for exception handling:
'''
try:
    code that can raise exception
except(Exception1, Exception2, Exception3,.....):
    code that executes if exception is raised
else:
      code that executes if exception is not raised
finally(optional):
    code that executes no matter what
raise: 
         raise keyword is used to raise an exception.
'''
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# try:
   
#     div=num1/num2
#     print(div)
# except exception as e:
#     print("Division by zero is not allowed")
    
# else:
#     print("End of the program")
# finally:
#     print("This is a finally block")
#output: Enter first number:10
#Enter second number:0
#Division by zero is not allowed
#This is a finally block

'''
Exception class:
- Exception class is the base class for all exceptions.


#to print exception class name:
#2 ways to print exception class name:
#1. using except block: e.__class__
#2. using sys module.
'''
#using except block:

# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# try:
#     div=num1/num2
#     print(div)
# except :
#     print(e.__class__)
#     print("Division by zero is not allowed")
# else:
#     print("End of the program")
# finally:
#     print("This is a finally block")
#output: Enter first number:10
#Enter second number:0
#<class 'ZeroDivisionError'>
#Division by zero is not allowed


#using sys module:

import sys
try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    div=num1/num2
    print(div)
except Exception as e:
    print(sys.exc_info())    
    print(sys.exc_info()[0])
    
    print("Division by zero is not allowed")

#output: Enter first number:10
#Enter second number:0
#<class 'ZeroDivisionError'>
#Division by zero is not allowed
#This is a finally block

#when finally block is not executed?
#when exception is not raised
#when we use exit() function in try block

#Types of exceptions:
'''
1. Built-in Exceptions:
    - ZeroDivisionError:
    - FileNotFoundError
    - ImportError
    - IndexError
    - NameError
    - TypeError
    - ValueError
    - FileNotFoundError
    - ImportError
    - KeyboardInterrupt
2. User-defined Exceptions:
    - CustomException
'''