# # '''
# # Modules  are  files containing Python code that can include classes ,functions , variables , etc 
# # modules behefit :
# # 1. Reusability
# # 2. Modularity   
# # 3. Encapsulation
# # '''  
# import math
# print(math.pi)
# print(math.e)
# print(math.sqrt(4))
# print(math.pow(2,4))
# print(math.log(10))
# print(math.sin(90))


# # #create a class define one function and variable again and again create one class and use their functions
# import math
# class MyMath:
#     def __init__(self):
#         self.pi=3.14
#         self.e=2.71
#     def getPi(self):
#         return self.pi
# class MyMath2:
#     def __init__(self):
#         self.m=MyMath()
#     def getPi(self):
#         return self.m.getPi()
   
# m=MyMath2()
# print(m.getPi())

# from math import *
# print("pi:")
# print(pi)
# print
# print(e)
# print("sqrt")
# print(sqrt(4))
# print("pow")
# print(pow(2,4))
# print("log")
# print(log(10))

# from math import pi,sqrt
# print(pi)
# print(sqrt(4))

# # Rename a module
# import math as m
# print(m.pi)
# print(m.sqrt(4))


# # create class having 3 functions : add , sub , mul  ang greet function  , import module file and whatever we did in this file we can use it in main.py file 
# class Calculator:
#     def add(self,a,b):
#         print("add")
#         return a+b
#     def sub(self,a,b):
#         print("sub")
#         return a-b
#     def mul(self,a,b):
#         print("mul")
#         return a*b

#     def greet(self):
#         print("Hello")


# #OS Module:
# # 1. OS module provides functions for interacting with the operating system.
# # 2. This module provides a portable way of using the operating system features, including file and directory operations, environment variables, and more.

# import os
# print("current working directory")
# print(os.getcwd())
# print("list of files and directories in current directory")
# print(os.listdir()) 

# # print("create a new directory")
# # os.mkdir("newdirectory")
# # print("directory created")

# # print("rename a directory")
# # os.rename("new directory","renamed directory")
# # print("directory renamed")

# print("delete a directory")
# os.rmdir("renamed directory")
# print("directory deleted")


#sys module:
# 1. sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys
# print("Python version")
# print(sys.version)
# print("Python version information")
# print(sys.version_info)
# print("Platform")
# print(sys.platform)
# print("Path")
# print(sys.path) 

# print("Exit")
# sys.exit("Exit the program") 
# print("Command line arguments")
# print(sys.argv)


from datetime import datetime,date,timedelta
print("current date and time :", datetime.now())
print("curent date :", date.today())
#get a date in string formatand convert it to date object
date_str = "2024-01-16"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj) 

# to perform arithmetic operations on date objects
# future_date = today()+timedelta(days=1)
# print(future_date)

#time module:
# 1. time module provides functions for working with time values.
import time
# print("current time")
# print(time.time())
# print("current time in seconds")
# print(time.ctime())
# print("sleep for 5 seconds")
# time.sleep(5)
# print("current time")
# print(time.ctime())