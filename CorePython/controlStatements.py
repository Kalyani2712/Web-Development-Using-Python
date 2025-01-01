# # #for loop to print fruit list
# # fruits=["mango","banana", "apple"]
# # for fruit in fruits:
# #          print("list of fruits :",fruit  )
# from http.cookiejar import uppercase_escaped_char
# from tkinter.font import names
#
# #Sum of number in list :
# # numbers=[1,2,3,4,5]
# # total=0
# # for number in numbers:
# #     total+=number
# # # print("total sum :",total, end="")
#
# #syntax for i in sequence
# # #wap program to display greatest number from list by using for loop :
# # numbers = [10, 13, 4, 90, 39, 50]
# # greatest_num = numbers[0]
# # for num in numbers:
# #     if num > greatest_num:
# #         greatest_num= num
# # print("The greatest number in the list is:", greatest_num) #output :90
#
#
#
# #syntax for i in range :
# #wap program to display greatest number from list by using for loop :
# # list=[10,13,4,90,39,50]
# # max=list[0]
# # for i in range(len(list)-1):
# #     if max<list[i+1]:
# #         max=list[i+1]
# # print(max)
#
#
#
# # Write a program to display even numbers from the list using for loop :
# # numbers = [28, 6, 4, 8,10, 13, 4,14, 90, 39, 50]
# # print("the Even Numbers are :")
# # # Iterate through the list
# # for num in numbers:
# #     if num % 2 == 0:
# #        print(num)
# #  #Output
# # The greatest number in the list is: 90
# # the Even Numbers are :
# # 28
# # 6
# # 4
# # 8
# # 10
# # 4
# # 14
# # 90
# # 50
#
# #
# # character = "KALYANI RAMESH KHANAVKAR"
# # count=0
# # for i in character:
# #     if i:
# #         count+=1
# # print("count of character (icluding space):",count)
# #
# # #excluding space :
# # character = "KALYANI RAMESH KHANAVKAR"
# # count = 0
# # for i in character:
# #     if i != " ":
# #         count += 1
# # print("Count of characters (excluding spaces):", count)
#
#
# #wap to display lowest numbrer
# # numbers = (10, 13, 4, 90, 39, 50)
# # lowest = numbers[0]
# # for num in numbers:
# #     if num < lowest:
# #         lowest = num
# # print("The lowest number in the tuple is:", lowest)
#
# # #print list of number from set :
# # numbers = {10, 13, 4, 90, 39, 50}
# # for num in numbers:
# #     print( num)
#
#
# #Dictionary :
#
# # student = {"name":"Kalyani Ramesh Khanavkar", "age":20, "Marks":9.90}
# # for key,value in student.items():
# #     print("the key value pair : ")
# #     print(f"{key}:{value}")
# #     print(student.keys())
# #     print(student.values())
#
# #====================RANGE FUNCTION
# #print first 5 from 0
# # for i in range(5):
# #     print(i)
#
#     # print
# # for i in range(10,0,-2):
# #     print(i,end="")
#
# #
# # sum_of_numbers = 0
# # for num in range(1, 11):
# #     sum_of_numbers += num
# # print("Sum of first 10 natural numbers:", sum_of_numbers)
#
# # print(range(5))
# # print(list(range(5)))
# # print(list(range(0,11)))
# # print(list(range(10,0,-1)))
#
#
# #20 december 2024
# #even Number printing between Series :
# #
# # num1 = int(input("Enter the first number: "))
# # num2 = int(input("Enter the last number: "))
# # for num in range(num1, num2 + 1):
# #     if num % 2 == 0:
# #         print(num)
#
# #between them exlude start and stop
# #
# # num1 = int(input("Enter the start number: "))
# # num2 = int(input("Enter the end number: "))
# # for num in range(num1 + 1,   num2):
# #     if num % 2 == 0:
# #         print(num)
#
#
# #WHILE LOOP :
#
#
# #PRINT 1TO 10 :
# # numbers = []
# # num = 1
# # while num <= 10:
# #     numbers += [num]
# #     num += 1
# # print(numbers)
# #
# # #infinit loop
# #
# # while True:
# #     names=input("Enter name :")
# #     if names:
# #         print(names)
# #
# #     else:
# #
# #         break
#
#
#
# # for i in range(0,10):
# #     print(i ,end="  ")
# #     if i==5:
# #             break
#
# #
# # for i in range(0,10):
# #     print(i ,end="  ")
# #     if i==5:
# #                    continue
#
#
#
# # while True:
# #     num=int(input("enter Number greater than 0:"))
# #     if num>0:
# #         break
# # print(num)
#
# #FUNCTIONS:
#
# #syntax
# # def function_name ():
# #     #code
# # function_name()
#
# # def greet():
# #     print("good morning")
# # greet()
# # def greet(name,age):
# #     print(f"hello {name}, your age is {age}")
# #
# # greet("kalyani",20)
#
# # def add(*nums):
# #     total=sum(nums)
# #     print(total)
# # add(2,4)
#
# #cube
# # def cube(n):
# #     return n ** 3
# # number = float(input("Enter a number: "))
# # print(f"The cube of {number} is {cube(number)}")
# #
#
#
# #square
# # def square(n):
# #     return n ** 2
# # result = square(5)
# # print("the square is : ",result)
#
# #
# # def calculate(a,b):
# #     sum=a+b
# #     diff=a-b
# #     return sum,diff
# # sum_answer,diff_ans=calculate(10,2)
# # print(f"Sum:{sum_answer}, diff :{diff_ans}")
#
# #Lamda function :
# # lambda arguments: expression   (syntax )
# #
# # double =lambda x:x*2
# # print(double(10))
# #
# # add =lambda x,y :x+y
# # print(add(3,10))
# #
# #
# # #Default argument
# # add =lambda x,y=2 :x+y
# # print(add(3,4))
#
# #basic lambda functions :
# # 1.filter > filter element in a collection based on condition
# # numbers =[1,2,3,4,5,6,7,8]
# # even_number =list(filter(lambda x:x%2==0,numbers))
# # print(even_number)
# #
# # #map fun > apply
# # numbers =[1,2,3,4,5,6,7,8]
# # square =list(map(lambda x:x**2,numbers))
# # print(square)
# #
# # # sorted()
# #
# # students = [("Kalyani",20),("xyz",27),("abc",16)]
# # sorted_stud = sorted(students, key=lambda x:x[1])
# # print(sorted_stud)
# #
# #
# # students = [("Kalyani",20),("xyz",27),("abc",16)]
# # sorted_stud = sorted(students, key=lambda x:x[0])
# # print(" first index x[0] :",sorted_stud)
# #
# # #to sorting in descending order
# # students = [("Kalyani",20),("xyz",27),("abc",16)]
# # sorted_stud = sorted(students, key=lambda x:x[1], reverse=True)
# # print("descending :",sorted_stud)
#
#

toupper=lambda s:s.upper()
print((toupper("kalyani")))

# Lambda function to find the square of a number
square = lambda x: x ** 2
print(square(4))  # Output: 16
print(square(9))  # Output: 81
