''' Iterator :
An iterator is an object that allows you to iterate over a collection of elements.
In Python, an iterator is an object that implements the iterator protocol, which consists of two methods:


iteration :
 iteration is a process of one element at a time.
 using collections like tuples,lists,sets,generator ,etc
'''
# numbers=[1,2,3,4,5]
# for num in numbers:
#     print(num,end=" ")

'''
 iterable :
 iterable is a collection of elements that can be iterated over.
it is an object that can return Iterator using Iter() method
__iter__() method returns an iterator object
''' 
# from collections.abc import Iterable

# numbers=[1,2,3,4,5]
# print(isinstance(numbers,Iterable)) #True

# #Normal list is not iterable
# a=10
# print(isinstance(a,Iterable))#False


#Iterator : 
# it is an object that give item one by one method of iterator :
# __next__() method returns the next item of iterator in sequence
# __iter__() method returns the iterator object itself 
#__next__() method raises StopIteration exception when iteration is over

#Example :

numbers=[1,2,3,4,5]
iterator=iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) 
print(next(iterator))
#output :
# 1
# 2
# 3
# 4
# 5 
# Traceback (most recent call last):
#   File "D:\python\iterator.py", line 33, in <module>
#     print(next(iterator))
# StopIteration 






