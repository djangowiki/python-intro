# File Handling in Python.

# a more effiecient way of data and information.
# Handling files in Python can be in two modes: text and binary

# We will be concentrating more on text files.
# We will learn the following: how to create a file, open a file, read a file, write to a file, append to a file,
# close a file and delete a file.

# Python inbuilth open function.
# We use this function to open files into our application.
# With this open() function we can have access to files into our application we want to read from, or want to
# write to or want to perform all other file handling operations.

# How to use the open() function.
# We start by invoking it and parsing a compulsory argument which is the name of the file.
# open("file.txt")
# Immediatlely we do this, python opens the file and it opens it just for reading.
# The second argument is the mode of the file. r stands for reading and t stands for text file. ie. the file should
# read as a text file.
# So basically, we open a file by first parsing in the name of the file and secondly, the mode in which the file should
# be handled.
# Code
# open("file.txt", "rt")

# File Opening Operations in Python.
# Character, Operation File Does(n't) Exist
# r  read   error
# a  append creates new file
# w  write  creates new file
# x  create exits throws error, does not exit creates new file.

# Character Mode
# t   text
# b   binary

# Working with Files in Python
# Its always important to have the file we want to handle to be in the same directory as our Python script.

# Python Read Operation using the read() method
# a_file = open("data_file.txt")
# a_file2 = open("data_file.txt", "rt") #rt is actually read and text mode which is just default values.
# print(a_file)
# We use the open function to open the file we want to read and store it in a variable.
# We then use the read function to actually read the contents of the file;
# r_file = a_file.read()
# print(r_file)

# Python Read Operation using the readline() method.
# a_file = open("data_file.txt")
# file_data = a_file.readline()
# print(file_data)

# The readline() only reads the first line. Let's read everything
# for file_ in file_data:
# print(file_)

# Python Write Operation.
# In Python, there are two ways we can write to a file. The first method is to overwrite and the second method is
# append.

# How to Overwrite A File in Python.
# a_file = open("data_file.txt", "w")
# a_file.write("Hello Python")

# How to Append to A File in Python
# a_file = open("data_file.txt", "a")
# a_file.write("\nLearning Python is Fun")

# How to Create A New File in Python
# a_file = open("data_file_1", "x")
# a_file.write("Hello Python Again")

# How to Remove A File in Python.
# import os

# os.remove("data_file_1")

# However, we need to make sure that the file exists before using the os.remove() method.

# Better Way to Remove A File in Python
import os

if os.path.exists("data_file_1"):
    os.remove("data_file_1")
else:
    print("File does not exists")
