# age=18
# if age >=18 :
#     print("egilible for vote ")
# else:
#     print("no vote ")
#
#

# Input the score
# score = float(input("Enter the score (out of 100): "))

# Determine the grade using if-elif-else
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# elif score >= 50:
#     grade = "E"
# else:
#     grade = "F"
#
# # Output the grade
# print(f"The grade for a score of {score} is {grade}.")

#positve : even no , negative , zero
# Input a number
# number = float(input("Enter a number: "))
# if number > 0:
#     print(f"The number {number} is positive.")
#     if number%2==0:
#         print("Even Number")
# elif number < 0:
#     print(f"The number {number} is negative.")
# else:
#     print(f"The number {number} is zero.")

#Ternary Operator :
#
# num =11
# res = "Even"if num%2==0 else "Odd"
# print(res)

# a=10
# b=20
# result = a if a>b else b
# print(result)
#
#
# age =int(input("enter Age"))
# result = "eligible to vote "if age>=18 else "Not eligible"
# print(result)

# Input the number
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
#

# num to check if a number is prime

# def is_prime(num):
#     if num <= 1:
#         return False
#     else :
#      for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# def is_prime(num):
#     if num <= 1:
#         return False
#     else :
#      for i in range(2,int( num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True
#
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
#


# def prime_till_n(n):
#     for num in range(2, n + 1):
#         if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):  # Check divisibility
#             print(num, end=" ")

# # Input
# n = int(input("Enter the value of n: "))
# prime_till_n(n)


def is_prime(num):
    if num <= 1:
        return False
    else :
     for i in range(2,int( num**0.5)+1):
        if num % i == 0:
            return False
    return True
def prime_n(n):
    count=0
    num=1
    while count<n:
        num+=1
        if is_prime(num):
            count+=1
    return num
print(prime_n(13) )