# A function is simply a group of code that is written to achieve a specific task.
# How to write a function in python


# def greet():
#     print("Hello World!")


# greet()

# Remember in Python, scope is defined by tabs and not curly braces like other programming languages.

# Why we need functions
# The main reason is for code-reuseability.

# Functions: Return Statement.
# def add_num():
#     sum_ = 2 + 3
#     return sum_


# returned_num = add_num()  # this is the same thing as saying returned_num = 5

# When you want to get the value returned when you invoked a function, just store the invocation in a variable.


# def greeting():
#     name = input("Enter your name: ")
#     message = "What's up ", name
#     return message


# gretting_invoke = greeting()
# print(gretting_invoke)

# Function Parameters.
# A function parameter is the variable we pass to a function.
# A function argument is the value we pass to a function when it is invoked.


# def greet(name):
#     return "What's up? " + name


# user_name = input("Enter your name: ")
# greeting = greet(user_name)
# print(greeting)

# Function with more than one parameter and argument.
# def greet(name, gender):
#     if gender == "male":
#         title = "Mr. "
#     else:
#         title = "Ms. "
#     greeting = "What's up " + title + name
#     return greeting


# user_name = input("Enter your name ")
# user_gender = input("Enter your gender ")
# message_result = greet(user_name, user_gender)
# print(message_result)

# A function can take more than two arguments and can take more than two parameters.
# The order of the arguments should match the order of the parameters.

# Function Keyword Arguments
# The keyword argument is used when you dont want to bother about the arrangement of the arguments.
def greet(name, gender):
    if gender == "male":
        title = "Mr. "
    else:
        title = "Ms. "
    greeting = "What's up " + title + name
    return greeting


user_name = input("Enter your name: ")
gender_ = input("Enter your gender: ")

greeting_msg = greet(name=user_name, gender=gender_)
print(greeting_msg)
# So with Keyword argument, we don't have to worry about the order of the parameters.

# Functions: Variable Scope.
# A variable scope is simply the different parts we can have access to the variable in the appplication
# Types of variable scope: Global Scope and the Local Scope.
# In python, a variable that has been decalred in the global scope cannot be updated in the local scope.
# The only way we can do that is by using the global keyword.

# Variable Scope Codes:
name = "Gabriel"  # global variable
print(name)
name = "Ikenna Gabriel"  # variable updated.


def variable_scope():
    global name
    name = "Ikenna Gabriel Ifenna"
