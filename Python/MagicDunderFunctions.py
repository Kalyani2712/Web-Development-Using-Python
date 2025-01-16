'''
 Magic and Dunder Functions
Def''' 
# #1.__init__()
# class student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
# s1=student("kalyani",1)
# print(s1.name)
# print(s1.rollno)

# # 2.__str__()
# # return the object in string format

# class student:  
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#     def __str__(self):  
#         return f"name :{self.name}, rollno: {self.rollno}"

# s1=student("kalyani",27)
# print(s1)


# class Adder :
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         print("add called")
#         return self.a+other.a,self.b+other.b

# a=Adder(10,20)
# b=Adder(30,40)
# print(a+b)
class Adder :
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        new_a=self.a+other.a
        new_b=self.b+other.b
        return Adder(new_a,new_b)
    def __str__(self):
        return f"a: {self.a}, b: {self.b}"

a=Adder(10,20)
b=Adder(30,40)
print(a+b) 



#complex number : c1- 5i+3j c2- 3i+2j  output-  by using dunder function

class Complex:
    def __init__(self,real,imaginary):
        self.real=real  
        self.imaginary=imaginary
    def __add__(self,other):
        return Complex(self.real+other.real,self.imaginary+other.imaginary)
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
c1=Complex(5,3)
print(c1)
c2=Complex(3,2)
print(c2)
print(c1+c2)

#__eq__() to check whether two objects are equal

class Complex:
    def __init__(self,real,imaginary):
        self.real=real  
        self.imaginary=imaginary    
    def __eq__(self,other):
        return self.real==other.real and self.imaginary==other.imaginary
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
c1=Complex(5,3)
print(c1)
c2=Complex(3,2) 
print(c2)
print(c1==c2)


# 
class student :
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def __eq__(self,other):
        return self.name==other.name and self.rollno==other.rollno
    def __str__(self):
        return f"name :{self.name}, rollno: {self.rollno}"
    def __gt__(self,other):
        return self.rollno>other.rollno
    def __lt__(self,other):
        return self.rollno<other.rollno
        def __ge__(self,other):
            return self.rollno>=other.rollno
        def __le__(self,other):
                return self.rollno<=other.rollno    
s1=student("kalyani",27)
s2=student("kalyani",27)
print(s1)
print(s2)

print(s1==s2) 
print(s1>s2)
print(s1<s2)
print(s1>=s2)
print(s1<=s2)


