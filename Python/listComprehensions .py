print("list Comprehensions")

# squares = [x**2 for x in range(1,11)]
# print(squares) 

# --------------------------------------------------
#Conditional List Comprehension
# --------------------------------------------------        
# even_list = [x for x in range(1,11) if x%2==0]
# print(even_list)

# --------------------------------------------------
#if-else List Comprehension
# --------------------------------------------------     
# display odd and even numbers with numbersfrom 1 to 10

# numbers = ["EVEN" if x%2==0 else "ODD" for x in range(1,11)]
# print(numbers) 

# --------------------------------------------------
#Nested List Comprehension
# -------------------------------------------------- 
# list_2d= [[j for j in range(1,4)] for i in range(3)]
# print(list_2d) 

#explaination:
'''
list_2d= [[j for j in range(1,4)] for i in range(3)]
print(list_2d) 
how it works:

[1,2,3]
[1,2,3]
[1,2,3]
 ''' 
#generate table of 2 till 10

# table = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(table) 
# #generate table of 1 to 5
# table = [[i*j for j in range(1,6)] for i in range(1,6)]
# print(table)
# --------------------------------------------------
#flatten List without  list Comprehension
# --------------------------------------------------
#combine all elements from mult
# list= [[1,2,3],[4,5,6],[7,8,9]]
# flat_list = []
# for row in list:
#     for x in row:
#         flat_list.append(x)
# print(flat_list)

#flatten with list comprehension
# flat_list = [x for row in list for x in row]
# print("Flattened list:",flat_list)

#Conditional List Comprehension
#print only even numbers from nested list :
# even=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
# flat_list = [x for row in even for x in row if x%2==0]
# print("Flattened list of even numbers :",flat_list) 

# #if-else List Comprehension
# list= [[1,2,3],[4,5,6],[7,8,9]]
# flat_list = ["EVEN" if x%2==0 else "ODD" for row in list for x in row]
# print("Flattened list of even and odd numbers :",flat_list)

#even (sir way)
# flat_list = [[j for j in range(1,11) if j%2==0] for i in range(3) ]
# print("even numbers from 1 to 10:",flat_list)

#Dictionary Comprehension
#syntax : dict = {key:value for key in sequence if condition}
#Square of numbers
dict = {x:x**2 for x in range(1,11)}
print(dict)

#Cube of numbers
dict = {x:x**3 for x in range(1,11)}
print(dict)

#if-else
dict = {x:"EVEN" if x%2==0 else "ODD" for x in range(1,11)}
print(dict)
#if 
dict = {x:"EVEN" if x%2==0 else "ODD" for x in range(1,11) if x%2==0}
print(dict)

#table of 2
dict = {x*y for x in range(1,11) for y in range(1,11)}
print(dict)

# 3. Transforming an Existing Dictionary
# Double the values of an existing dictionary:

original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
print(doubled)


# 4. Swapping Keys and Values
# Create a dictionary by swapping keys and values:
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)

# 5. From Two Lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
combined = {k: v for k, v in zip(keys, values)}
print(combined)

# Nested Dictionary Comprehension
table = {x: {y: x * y for y in range(1, 6)} for x in range(1, 4)}
print(table)