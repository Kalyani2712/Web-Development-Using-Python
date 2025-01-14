#File Handling in Python 
'''
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
Syntax
To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")
The code above is the same as:
f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.
Note: Make sure the file exists, or else you will get an error.

'''
#Opening a file
# data=open("file.txt","r")
# print(data.read())
# data.close()
#Writing to a file
# data=open("file.txt","w")
# data.write("Hello World")
# data.close()
# #Reading a file
# data=open("file.txt","r")
# print(data.read())

# -------------------------------------------------------------
# #Reading a file line by line
#using with block -> there is no need to close the resources gets automatically closed
#with open("file.txt","r") as file:
#     print("Reading a file line by line")
#     for line in file:
#       print(line,end="")

'''
        Characters :
        r - Read - Default value. Opens a file for reading, error if the file does not exist
        a - Append - Opens a file for appending, creates the file if it does not exist
        w - Write - Opens a file for writing, creates the file if it does not exist
        x - Create - Creates the specified file, returns an error if the file exists
        Modes:
        t - Text - Default value. Text mode
        b - Binary - Binary mode (e.g. images)
        + - Read and Write
                
''' 

        #Writing to a file (example.txt)

# with open("example.txt", 'w') as file :
#             file.write("This is first line.\n")
#             file.write("This is second line.\n")
#             file.close
#             print("File created successfully - write")
# with open("example.txt", 'r') as file :            
#             print(file.read())
#             file.close
#             print("File read successfully-read")
# with open("example.txt", 'a') as file :
#             file.write("This is third line which is appended.\n")
#             file.close
#             print("File appended successfully")


# create a file "practice.txt" and write to it

with open("practice.txt", 'w') as file :
    file.writelines(["Hello Everyone.\n","we are learning file I/o.\n","Using Java.\n","I like programming in Java. \n"])

#Replace all Occurrences of a Java with Python:
with open("practice.txt", 'r') as file :
    data=file.read()
    newdata=data.replace("Java","Python") 

#Overrite the file
with open("practice.txt", 'w') as file :
    data=file.write(newdata)
Word = "programming"
with open("practice.txt", 'r') as file :
    data=file.read()
    if(data.find(Word) != -1):
       print("Word found")
    else:
        print("Word not found")
