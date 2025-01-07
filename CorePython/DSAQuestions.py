# # 1. Check if a string is a palindrome (ignoring spaces and case)
# # Program :
# def is_palindrome(s):
#     s = ''.join(filter(str.isalnum, s)).lower()
#     return s == s[::-1]
# print(is_palindrome("A man a plan a canal Panama"))  # True
# print(is_palindrome("hello"))  # False
# print(" ---------------------------------------------------")
# # 2.Check if two strings are anagrams:
# # Program :
# def are_anagrams(s1, s2):
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     return sorted(s1) == sorted(s2)

# print(are_anagrams("Listen", "Silent"))  # Output: True
# print(are_anagrams("Hello", "World"))   # Output: False

# # print("---------------------------------------------------")
# # # 3.Find the first non-repeating character in a string
# # # Program :
# # def first_non_repeating(s):
# #     s = s.lower()
# #     for char in s:
# #         if s.count(char) == 1:
# #             return char
# #     return None

# # print(first_non_repeating("swiss"))  # Output: w
# # print(first_non_repeating("aabbcc"))#Output:None 
# # print("---------------------------------------------------")

# # # 1. Check if two strings have common characters
# # str1 = "hello"
# # str2 = "world"
# # common = not set(str1).isdisjoint(set(str2))
# # print(f"Do the strings have common characters? {common}")  # Output: True
# # print("---------------------------------------------------")

# # # 2. Convert a list of tuples to a dictionary
# # lst = [("a", 1), ("b", 2), ("c", 3)]
# # dictionary = dict(lst)
# # print(f"Dictionary: {dictionary}")  # Output: {'a': 1, 'b': 2, 'c': 3}
# # print("---------------------------------------------------")

# # # 3. Sort a dictionary by its values in ascending order
# # sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
# # print(f"Sorted Dictionary: {sorted_dict}")  # Output: {'b': 1, 'c': 2, 'a': 3}
# # print("---------------------------------------------------")


# # 4. Create a Rectangle class with attributes length and width. Use the constructor to initialize these attributes.
# # class Rectangle:
# #     def __init__(self, length, width):
# #         self.length = length
# #         self.width = width

# #     def area(self):
# #         return self.length * self.width

# #     def perimeter(self):
# #         return 2 * (self.length + self.width)
# # rectangle = Rectangle(5, 3)
# # print(f"Area of Rectangle: {rectangle.area()}")          # Output: 15
# # print(f"Perimeter of Rectangle: {rectangle.perimeter()}")  # Output: 16
# # print("---------------------------------------------------")
# # 2. Create a class SumNumbers that contains two attributes num1 and num2, and a method sum() that returns the sum of these two numbers.

# # class SumNumbers:
# #     def __init__(self, num1, num2):
# #         self.num1 = num1
# #         self.num2 = num2

# #     def sum(self):
# #         return self.num1 + self.num2


# # numbers = SumNumbers(10, 20)
# # print(f"Sum of numbers: {numbers.sum()}")  # Output: 30
# # print("---------------------------------------------------")
# # 3. Create a class Calculator with methods add(), subtract(), multiply(), and divide() to perform basic arithmetic operations.

# class Calculator:
#     def add(self, num1, num2):
#         return num1 + num2

#     def subtract(self, num1, num2):
#         return num1 - num2

#     def multiply(self, num1, num2):
#         return num1 * num2

#     def divide(self, num1, num2):
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Cannot divide by zero"
# calc = Calculator()
# print(f"Addition: {calc.add(10, 5)}")           # Output: 15
# print(f"Subtraction: {calc.subtract(10, 5)}")   # Output: 5
# print(f"Multiplication: {calc.multiply(10, 5)}") # Output: 50
# print(f"Division: {calc.divide(10, 5)}")         # Output: 2.0


#DSA Questions:
# 1) Check if string contains all unique characters. 
def unique_chars(s): 
    return len(set(s)) == len(s) 
print(unique_chars("hello")) # False 
print(unique_chars("world"))  # True
# 2) Print all possible permutations of a string.
from itertools import permutations
def permute(s):
    return [''.join(p) for p in permutations(s)]
print(permute("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# 3) Find symmetric difference of two sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)  # Output: {1, 2, 5, 6}

