# #Dictionary :
# '''
# #collection of Key-value pair , unordered , mutable , not allow duplicate keys ;
# #keys ->  Immutable(string , tuple ,etc) , Values -> it can repeat or any data Type
# #Creating A dictionary :
# there are 2 ways :
# 1.using Curly braces ({})
# 2. using Dictionary function -> dict()
# '''
# # 1.using Curly braces ({})
# student = {"name": "kalyani" , "age ":20 , "city":"panvel"}
# # print(student)
# # print(type(student))
#
# #Type 2 : using dict()
# employee=dict(id=101,name="kalyani")
# # print(employee)
# # print(type(employee))
#
#
# #Dictionary Functions:
#
# #1.keys():
#
# # print("keys :",student.keys())
# # print("keys  :",employee.keys())
#
# #Values():
#
# # print("values :",student.values())#output :values : dict_values(['kalyani', 20, 'panvel'])
# # print("values :",employee.values())#Output:values : dict_values([101, 'kalyani'])
#
# #items() -> it will return key value pair as tuple
#
# # print(student.items())
#
# #get() -> it will return value for specified key .
#
# # print("value of key name: ",student.get("name"))
#
# #update(): update the dictionary with new  key value pair
# student.update({"city":"Banglore"})
# print(student)
#
# #Pop(): remove key-value pair  from pair based on key :
# student.pop("city")
# print(student)

#Traversing in a Dictionary
student1 = {"name": "kalyani" , "age ":20 , "city":"panvel"}
print(student1)
#Traversing Keys :
# Way 1 :
for key  in student1:
    print(f"keys :{key},values : {student1[key]}")
#way 2 :
print("Way 2 : -------------------------------------")
for key,value  in student1.items() :
    print(f"key : {key}, value :{value}")

#Difference between  list and  Dictionary :
'''
1. dictionary is collection of key value pair 
list is  collection of ordered items 

2. dictionary defined using curly  braces ({}) and 
list using square braces([])

3. dictionary  accessed by keys and list by index

4,  list allow duplicate values 
 dictionary keys are uniques , value can be duplicates
 




'''