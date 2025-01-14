'''
Generators are functions that return an iterator object, which can be used to iterate over a sequence of values.
Generators are created using the yield keyword, which returns a value and suspends the function's execution.
keypoints :
1.generators are lazy evaluated , they are not executed until they are iterated over
2.generators are memory efficient , they use less memory than a list
3.generators are faster than list comprehensions , they are more efficient for large datasets
4.using yield keyword in a function makes it a generator

'''
#Simple way to creat a list for no 1 to 1000
#create a list for number 1 to 1000 
import sys
# def generate_numbers():
#     list=[]
#     i=1
#     while i<=100:
#         list.append(i)
#         i+=1
#     return list

# list=generate_numbers()
# print(list)
# size=sys.getsizeof(list)
# print("size of list in bytes:",size)#size of list in bytes: 920

#using generators
# def generate_numbers(n):
#     i=1
#     while i<=n:
#         yield i
#         i+=1
# list=generate_numbers(100)
# for i in list:
#     print(i)
# size=sys.getsizeof(list)
# print("size of list in bytes:",size)#size of list in bytes: 192

#create a lis :
# new_list =list(range(1,11))
# print(new_list) 
# size=sys.getsizeof(list)
# print("size of list in bytes:",size)


#using generators
# def generate_numbers(n):
#     i=1
#     while i<=n:
#         yield i
#         i+=1

# gen=generate_numbers(100)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(list(gen))

#Output :
# 1
# 2
# 3
# 4
# 5
#[6,7,.....,100]

#Create a  fibonacci series using generators

# #without using generators
# def fibonacci(n):
#     a,b=0,1
#     for i in range(n):
#         print(a , end=" ")
#         a,b=b,a+b

# fibonacci(8) #0 1 1 2 3 5 8 13




#using generators   
# def fibonacci(n): 
#     a,b=0,1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# for i in fibonacci(8):
#     print(i,end=" ") 

#Generator Expression:
#similar to list comprehension but instead of creating a list [], it creates a generator object ()

#generatning squares using list comprehension
# squares = [x**2 for x in range(1,11)]
# print(squares)    

#using generators
squares = (x**2 for x in range(1,11))
print(squares)#<generator object <genexpr> at 0x7f8c9b4d4f60>
for i in squares:
    print(i,end=" ")#1 4 9 16 25 36 49 64 81 100 

'''
#Summary :
List Approach :
1.Creates a list in memory
2.Creates a copy of the list in memory

Gnerator Approach :
produce number one by one therefore it is more memory efficient
1.Creates a generator in memory
2.Creates a copy of the generator in memory
we use Generator when i dont want to store the entire list in memory and can process them one by one
'''