'''
Tuple ->  it is an immutable collection of items .
          we cannot add , remove or modify.
          it is Ordered
          tuple is defined using Parantheses ()
'''

#Create a tuple :
name = ("Ram ","sham ", "Naman")
print(name) #Output : ('Ram ', 'sham ', 'Naman')
print(type(name)) #Output : <class 'tuple'>

#Create A Tuple having single Element :
tuple =(28 ,)
print(tuple) #Output : (28,)
print(type(tuple)) #Output : <class 'tuple'>

#Traversing in Tuple :
name = ("Ram ","sham ", "Naman")
print(name[0] )  #Output : Ram
print(name[-1])  #Output : Naman

#Concatination :

a= (1,2,10,3, 2,2, 10)
b=(20, 23,21)
print("Concatination of Tuple  a and b : ",a+b) #Output :Concatination of Tuple  a and b :  (1, 2, 10, 3, 2, 2, 10, 20, 23, 21)

#print multiple time the tuple using asterisk (*) symbol :

print(a*2) #Output : (1, 2, 10, 3, 2, 2, 10, 1, 2, 10, 3, 2, 2, 10)

#Membership operation on Tuple :
print(10 in a)  #Output : True
print(20 not in b)  #Output : False
#Length of Tuples :
print("length of a :",len(a)) #Output : length of a : 7
print("length of b :",len(b)) #Output : length of b : 3
#Min value :
print("minimum value  of a :",min(a)) #Output : minimum value  of a : 1
#Max value :
print("maximum value of a :",max(a)) #Output : maximum value of a : 10
#Count Number of element in Tuple :
print("number of element 2 in a :",a.count(2)) #Output : number of element 2 in a : 3
#position of Element
print("position of element 10 in  at index  :",a.index(10)) #Output : position of element 10 in a  at index : 2
#Slicing :
a1 = (1, 2, 10, 3, 2, 2, 10)
print(a[1:4]) #Output : (2, 10, 3)
#Reversing :
print(a[:: -1]) #Output : (10, 2, 2, 3, 10, 2, 1)
'''
Why to use Tuple ? 
1. Tuple is faster than list
2. Tuple ensures the integrity of data 
'''