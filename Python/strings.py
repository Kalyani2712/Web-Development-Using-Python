# s1="hello"
# print(s1)
# # s2='hii'
# print(s2)
# s3='''This is first line
#   this is a second line
#  this is a third line '''
# print(s3)
#
#
from os.path import split

# string1 = "Kalyani Ramesh khanavkar"
# print("string1 :",string1)
# #Slicing
# print("char 2 :",string1[2])
# print("char 1 :",string1[0])
# print("str last : ",string1[-1])
#
# #Indexing
# print(string1[6:18])
# print(string1[3:])#end by default
# print(string1[:18])#start by default

#concatination
# str1="hello"
# str2="world"
# res=str1+str2
# print("concatination : ",res)

#Repetition(*)
# str1="hello"
# print("repetition :",str1*3)

#membership operators
# name="kalyani khanavkar "
# print("kalyani"in name)#true
# print("kalyani" not in name)#false

#comparisions(< >= >_)
# s1="apple"
# s2="banana"
# print(s1==s2 )#false
# print(s1 >s2)#false
# print(s1 <s2)#true

#
# s1="apple"
# s2="Banana"
# print(s1==s2 )
# print(s1 >s2)
# print(s1 <s2)

# s="cat"
# s1="caterpillar"
# print(s > s1)
# print(s < s1 )

# print(ord('A')) #65
# print(ord('B'))#66
# print('A' < 'a')#true
# print("abc" >"ABC")#true
# print(ord('a'))#97
# print(ord('0'))#48


# print("abc".lower() =="ABC".lower())
# print("abc".upper() =="ABC".upper())
# s="my name is kalyani "
# for char in s :
#     print(s)


#string functions :

# 1. len > return length of string
# string="my name is kalyani "
# print(len(string)) #19 but start from 0 so ..18

#by using  range function how to do iteration on string
# my_string = "Hello"
# for i in range(len(my_string)):
#     print(my_string[i])

#using Loop :
# word = "Kalyani Ramesh Khanavkar "
# for char in word :
#     print(char)


# String functions :
#
# string="kalyani Ramesh Khanavkar"
# str="python is fun"
# print("length :",len(string))
# print("length of str:", len(str))
# print("upper case:",string.upper())
# print("lower case :",string.lower())
# print("capitalize 1st letter of word :",string.capitalize())
# print("capitalize all first letter : ",string.title())
# print("Remove start and End :", string.strip())
# print("replaced string : ",str.replace("fun", "Casesensitive"))
# print("split the string : ",str.split())
# string_list =  ['python', 'is', 'fun']
# print("joines list :", "".join(string_list))
# print("starts with : ",str.startswith("py"))
# print("ends with : " , str.endswith("fun"))

#Reverse a string
# strin="hello"
# print(strin[: : -1 ])

#Palindrome
#check whether a string is pralindrome or not :
# word = input("enter a string :")
# if word ==word[::-1]:
#            print("its palindrome ")
# else:
#     print("its Not palindrome ")

#count the vowels  in a string :
# vowel ="aeiouAEIOU"
# string="python programming "
# count = 0
# for char in string:
#         if char in  vowel:
#                         count+=1
# print("total count of vowels  is :  " ,  count)


 # string format operators :
 #reverse string



# Q1: Reverse words in a string

# def reverse_words(s):
#     return " ".join(s.split()[::-1])
#
# string = "python is fun"
# output = reverse_words(string)
# print(output)
# Reverse Each Word in the String Q2
# def reverse_each_word(s):
#     words = s.split()
#     reversed_words = [word[::-1] for word in words]
#     return " ".join(reversed_words)
# string = "python is fun"
# output = reverse_each_word(string)
# print(output)  # Output: nohtyp si nuf

# Q3: Reverse the string without using any built-in functions
# def reverse_string(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s
#     return reversed_s
#
# string = "python is fun"
# output = reverse_string(string)
# print(output)


# Q4: Reverse string with isalpha() constraint

# def reverse_alphabets(s):
#     alphabets = [char for char in s if char.isalpha()]
#     reversed_alphabets = alphabets[::-1]
#     result = []
#     alpha_index = 0
#     for char in s:
#         if char.isalpha():
#             result.append(reversed_alphabets[alpha_index])
#             alpha_index += 1
#         else:
#             result.append(char)
#     return ''.join(result)
#
# string = "a.byc3"
# output = reverse_alphabets(string)
# print(output)

# Reverse string with isalnum() constraint

# def reverse_alphanum(s):
#     alphanum = [char for char in s if char.isalnum()]
#     reversed_alphanum = alphanum[::-1]
#     result = []
#     index = 0
#     for char in s:
#         if char.isalnum():
#             result.append(reversed_alphanum[index])
#             index += 1
#         else:
#             result.append(char)
#     return ''.join(result)
#
# string = "a.byc3"
# output = reverse_alphanum(string)
# print(output)

#Swapping :


# 1. Using Slicing

# str1 = "Hello"
# str2 = "World"
# str1, str2 = str2[:], str1[:]
# print(str1, str2)  # Output: World Hello
#
# # 2. Using a Loop
# str1 = "Hello"
# str2 = "World"
#
# str1_list = list(str1)
# str2_list = list(str2)
#
# for i in range(len(str1_list)):
#     str1_list[i], str2_list[i] = str2_list[i], str1_list[i]
# str1 = ''.join(str1_list)
# str2 = ''.join(str2_list)
# print(str1, str2)  # Output: World Hello
#
# # 3. Using reversed()
#
# str1 = "Hello"
# str2 = "World"
# str1, str2 = ''.join(reversed(str2)), ''.join(reversed(str1))
# print(str1, str2)  # Output: dlroW olleH
#
# #4Using lambda
#
# str1 = "Hello"
# str2 = "World"
# swap = lambda x, y: (y, x)
# str1, str2 = swap(str1, str2)
# print(str1, str2)  # Output: World Hello
#
# #5 Without Temporary Variable
# str1 = "Hello"
# str2 = "World"
#
# str1, str2 = str2, str1  # Direct tuple swapping
# print(str1, str2)  # Output: World Hello
#
# #using 2 pointers :







#using isalpha():
def swap_alphabets(s):
    s = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    return ''.join(s)

string = "kalyani_2712"
output = swap_alphabets(string)
print(output)  # Output: "c.by3a"
