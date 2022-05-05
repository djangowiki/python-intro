# Python fStrings.

first_name = "Ifenna"
last_name = "Ikenna"

full_name = f"{first_name} {last_name}"

# print(full_name)

greeting_msg = "Good Morning,"
wife_name = "Blessing"
wife_last_name = "Fruebi"

wife_greeting = f"{greeting_msg} {wife_name} {wife_last_name}"
# print(wife_greeting)

# Escape Characters and Escape Sequences in Strings
# \n \t \

# Substrings in Python.
# We can check for a character using the in and the not in keywords. or presence of a substring within a string.ß
check_string = "Hello" in "Hello World"
# print(check_string)
check_string_not = "Hello" not in "Hello World"
# print(check_string_not)

# Strings as an arrays.
# In Python, strings are arrays.
# How to work with strings as arrays.
main_str = "I am a string"
# for char in main_str:
# print(char)

# print(main_str[1:-1])

# Python inbuilt function
# These functions help to make life alot easier for developers when working with strings in python
# lower(), swapcase(), upper(), title(), Istrip(), rstrip(), strip(), isspace(), count(), find()

# Alter the case of a string.
my_string = "Ikenna ifenna"
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.title())
# print(my_string.swapcase())

# Python methods for removing trailing white spaces.
my_stripe = " Hello World Gabby "
# print(my_stripe.rstrip())  # removes the trailing white space at the right
# print(my_stripe.lstrip())  # removes the trailing white space at the left
# print(my_stripe.strip())  # removes the trailing white space at the both sides.

# How Stripe Characters that are not white spaces.
# print(my_string.strip("I"))  # Python will only do this if that character is at the end.

# Python isspace() method
# We use this method to know if a python is made up of just white spaces or not.
# This method returns a boolean.
# It does not take any argument.
# The isspace method doesn't work for empty string ""

my_main_str = "I am a string"
# print(my_main_str.isspace())

# Python count() method
# Find out the number of times a character appeared in a string.
# We have to pass the char as an argument.

my_str_count = "Hello World"
# print(my_str_count.count("l"))

# Python find() method.
# It is used to find a charcter or sequence of characters in a string.
# It returns the index position of the first occurence.
# If a character is not found, -1 is returned.
# Another method that works like the find method is the index method.
# But the main difference between index and find is that, any character or sequence of character that is not
# found in the string throws an error.

find_str = "Hello World"

print(find_str.find("l"))
