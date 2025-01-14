#creating a list :
# list =[1,2,3,4,5,6,7]
# list1=[8,9,10,11,12,13,14]
# print("my list :",list)
# print(type(list))
# #concate
# print(list1+list)
# #repetition :
# print(list*2)
# #membership operator :
# print(2 in list )
# print(12 not in  list1)
# #slicing :
# print(list[1:5])
# print(list[:5])
# print(list[2:])
# print(list[:])
# print(list[::2])
# print(list[::-1])
# print(list[::-2])

# lst=[2,10,11,13,15,30]
#comman list functions :

# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sorted(lst))

# converting other data type into list :
# str ="hello "
# print(list(str))


fruits=[ "apple", "banana" , "pineapple","mango"]
# # append():
# fruits.append("kiwi")
# print(fruits)
#
# #insert():
# fruits.insert(-1,"orange") #opt :['apple', 'banana', 'pineapple', 'mango', 'kiwi']
# fruits.insert(1,"grapes")
# print(fruits)#output : ['apple', 'grapes', 'banana', 'pineapple', 'mango', 'orange', 'kiwi']
#
# #Remove():
# fruits.remove("grapes")
# print(fruits) #output :['apple', 'banana', 'pineapple', 'mango', 'orange', 'kiwi']
#
# #pop(): remove the element ;
# fruits.pop(2)
# print(fruits)
# print(fruits.pop(2))
#
# #Index():
# fruits.index("orange")
# print(fruits)
#
#
# #Count():
# print(fruits.count("Apple"))
# #reverse()
# fruits.reverse()
# print(fruits)
#
# #Clear():
# fruits.clear()
# print(fruits)
#Traversing :
#Traveraing in a list using for loop :
# list3 =["pink","blue", "yellow","Violet"]
# for color in list3:
#         print(list3)

#traversing wih index :
# for i in range(0,len(list3)):
#         print(list3[i])
#while loop :
list =[1,14,29,3,2]
i=0
while i < len(list):
    print(list[i])
    i+=1

