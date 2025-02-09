'''
RegEx stands for Regular Expression
A RegEx, or regular expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
import re - regular expression module
to work with regular expression we need to import re module
Uses :
1. to validate an email address
2. to validate a phone number 
use for 1. search and 2. replace
3. to find a pattern in a string
4. to split a string based on a separator
5. to join a list of strings
6.to get information from a string
''' 

# import re
# text="kalyani.khnavkar27@gmail.com"
# #To search a dot (.) in a string
# pattern = r"."
# result=re.findall(pattern,text)
# print(result)
# result1=re.search(pattern,text)
# print("By searching  :",result1) #By searching  : <re.Match object; span=(0, 1), match='k'>
# p=r"\." # to escape a special character dot (.)
# print(re.search(p,text))  #<re.Match object; span=(7, 8), match='.'>

# #Numeric value : usin \d -> for numerical value 
# pattern = r"\d+" 
# result=re.search(pattern,text)
# print(result)
# result1=re.findall(pattern,text)    
# print(result1) 
# #Output :<re.Match object; span=(21, 27), match='27@gmail'>
# # ['27', 'gmail']

# #Non Numeric value : usin \D -> for Non numerical value (0-9)
# text="ny number is 1234567890"
# pattern = r"\D+"
# result=re.search(pattern,text)
# print(result)
# result1=re.findall(pattern,text)    
# print(result1) 


# text="kalyani"
# pattern = r"\bkalyani\b"
# result=re.search(pattern,text)
# print(result)
# result1=re.findall(pattern,text)    
# print(result1)
# #Output :<re.Match object; span=(0, 6), match='kalyani'>
# # ['kalyani']

# #Whitespace : \s
# text="kalyani khnavkar"
# pattern = r"\s"
# result=re.search(pattern,text)
# print(result)
# result1=re.findall(pattern,text)    
# print(result1)
# # Output :<re.Match object; span=(7, 8), match=' '>
# # [' ']

# #Non Whitespace : \S
# text="kalyani khnavkar"
# pattern = r"\S"
# result=re.search(pattern,text)
# print(result)
# result1=re.findall(pattern,text)    
# print(result1)
# # Output :<re.Match object; span=(0, 1), match='k'>
# # ['k', 'a', 'l', 'y', 'a', 'n', 'i', ' ', 'k', 'h', 'n', 'a', 'v', 'k', 'a', 'r']

# #Alphabets : \w
# text="kalyani khnavkar"
# pattern = r"\w"
# result=re.search(pattern,text)
# print(result)
# result1=re.findall(pattern,text)    
# print(result1)
# # Output :<re.Match object; span=(0, 1), match='k'>
# # ['k', 'a', 'l', 'y', 'a', 'n', 'i', ' ', 'k', 'h', 'n', 'a', 'v', 'k', 'a', 'r']

# #Non Alphabets : \W
# text="kalyani khnavkar"
# pattern = r"\W"
# result=re.search(pattern,text)
# print(result)
# result1=re.findall(pattern,text)    
# print(result1)
# #Output :<re.Match object; span=(7, 8), match=' '>
# # [' ']

# text =" 10 * 8 = 80"
# pattern = r"10 *8"
# result=re.search(pattern,text)
# if result:
#     print("Pattern found") #output : Pattern not found
#     print(result)
# else:
#     print("Pattern not found")

# #match -> returns the first match
# text="hello i am kalyani khnavkar"
# pattern = r"hello"
# result=re.match(pattern,text)
# print(result)
# #Output : <re.Match object; span=(0, 5), match='hello'>

# #search -> returns the first match
# text="hello i am kalyani khnavkar"
# pattern = r"hello"
# result=re.search(pattern,text)
# print(result)
# #Output : <re.Match object; span=(0, 5), match='hello'>



# text="hello i am kalyani khnavkar my number is 1234567890"
# pattern="\d+"
# match=re.finditer(pattern,text)
# for i in match:
#     print(i)    
#     print(i.group())



# #substitute
# text="hello i am kalyani khnavkar"
# pattern = r"hello"
# result=re.sub(pattern,"hi",text)
# print(result)
# #Output : hi i am kalyani khnavkar

import re
#replace numbers with *******
# text="hello i am kalyani khnavkar my number is 1234567890 and 9876876554"
# print(text)
# pattern="\d"
# result=re.sub(pattern,"*",text)
# print(result)
#Output :
# hello i am kalyani khnavkar my number is ******** and ********


#Patern matching
# a) .(dot) : matches any single character except new line(\n)
# b) \.(dot) : matches any single character including new line(\n)
# text="abc , asc ,abbc , a!c , a\nc ,a.c "
# pattern = r"a.c"
# match=re.findall(pattern,text)
# print(match)
#Output : ['abc', 'asc', 'a!c', 'a.c']

# ^ (caret) : matches the beginning of the string
# text="hello , good morning"
# pattern = r"^hello"
# match=re.findall(pattern,text)
# print(match)
#Output : ['hello']

# $ (dollar) : matches the end of the string
# text="hello , good morning!"
# pattern = r" morning!$"
# match=re.findall(pattern,text)
# print(match)
# #Output : ['good morning!']


# * (asterisk) : matches zero or more occurrences of the preceding character
# text="abc , asc ,abbc , a!c , a\nc ,a.c "
# pattern = r"ab*c"
# match=re.findall(pattern,text)
# print(match)
# #Output :['abc', 'abbc']

# # + (plus) : matches one or more occurrences of the preceding character
# text="abc , abbbc , abac , abdc , abbc "
# pattern = r"ab+c"
# pattern1= r"ab*c"
# match=re.findall(pattern,text)
# print(match)
# #Output : ['abc', 'abbbc', 'abbc']
# match1=re.findall(pattern1,text)
# print(match1)
# #Output :['abc', 'abbbc', 'ac', 'abbc']

# ? (question mark) : matches zero or one occurrence of the preceding character
text="abc , ac , abbc "
pattern = r"ab?c"
match=re.findall(pattern,text)
print(match)
#Output :['abc', 'ac']

#[] (square brackets) : matches any one character inside the brackets
text="abd , acd, abcd,acbd"
pattern = r"a[bc]d"
match=re.findall(pattern,text)
print(match)
#Output :['abd', 'acd']

# (or) : matches any one character inside the brackets
text="abd , acd, abcd,acbd"
pattern = r"a[bcd]d"
match=re.findall(pattern,text)
print(match) 
#output : ['abd', 'acd']


# | (or) : matches any one character inside the brackets
text="abd , acd, abcd,acbd"
pattern = r"a|d"
match=re.findall(pattern,text)
print(match)
#output : ['a', 'd', 'a', 'd', 'a', 'd', 'a', 'd']

#homework 
# groups () : groups multiple expressions to match a single pattern
text="abd , acd, abcd,acbd"
pattern =r"(a)(b)(c)"
match=re.findall(pattern,text)
print(match)
#output : [('a', 'b', 'c')]