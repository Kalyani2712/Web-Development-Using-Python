'''
Set -> unordered collection of unique elements in python .
       Tuples are mutable ,but  elements of Tuple should be immutable
-unique
-Unordered
-Mutable
'''
#Creating A set :
set1 = {1,2,3,4,5,6,3,2}
print(" set :",set1 ) #Output:  set : {1, 2, 3, 4, 5, 6}
print("type of set :",type(set1))  #Output:type of set : <class 'set'>
#Way 2 : set() function
set2=set([2,4,6,8,10,2,6])
print("creating set usng fuction set() : ",set2) #Output: creating set usng fuction set() :  {2, 4, 6, 8, 10}

#Creating a Set having single element :
set3={20}
print("single element Set :",set3) #Output: single element Set : {20}
print("data type of Set :",type(set3)) #Output: data type of Set : <class 'set'>

#creating a Empty Set
set4= {} #Wrong Way
print("empty Set :",set4) #Output: empty Set : {}
print( type(set4)) #Output :<class 'dict'>

set5=set() #Correct Way
print(set5) #Output: set()
print(type(set5)) #Output: <class 'set'>

#Set Functions :
Set1 = {1,2,3,4,5,6,3,2}
#Add():
Set1.add(100)
print("Add :",Set1) #Output: Add : {1, 2, 3, 4, 5, 6, 100}
#Remove():
Set1.remove(3)
print("Remove :",Set1) #Output: Remove : {1, 2, 4, 5, 6, 100}

Set1.remove(7) # if element not found , it throws Error
print("Remove if element not exist :",Set1) #Output:  Set1.remove(7)
                                                      # ^^^^^^^^^^^^^
                                                      # KeyError: 7
#Discard():
Set1.discard(7) #if element not found , it doesn't throw error
print("Discard",Set1) #Output: Discard {1, 2, 4, 5, 6, 100}

#pop()-> it will remove Random Element
Set1.pop()
print("pop element from Set :",Set1) #Output: pop element from Set : {2, 4, 5, 6, 100}

#Clear()
Set1.clear()
print("Clear Set :", Set1) #Output: Clear Set : set()

#Set Operations :

set1 = {1,2,3}
set2={3,4,5}
#Union :
print("Union : ",set1 | set2 ) #Output :{1, 2, 3, 4, 5}
#Intersection:
print("Intersection:",set1  & set2 ) #Output : {3}
#symmetric_Difference() :
print(set1 ^ set2 ) #Output: {1, 2, 4, 5}
#Differnce() :
print(set1 - set2) #Output : {1, 2}

#Subset and Superset :
setA={1,2,3}
setB={1, 3}
print(setB.issubset(setA)) #Output :True
print(setA.issuperset(setB)) #Output :True
'''
Why to use Set And when to use Set ? 
1. if i Want any Unique Element ,we use Set 
2. Quickly check if element exist or not 
3. Efficient Execution of set Operations such as union , Intersection 
'''