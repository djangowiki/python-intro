# print(type("wejsdfnedfx"))
d_data = "1000"
# print(type(d_data))
d_data = True
new_data = str(d_data)
# print(type(new_data))

# String Concatenation.
first_name = "Ikenna"
last_name = "Ifenna"
age = 30

full_name = first_name + " " + last_name
# print(full_name)

name = "{} {}"
name_age = "{} {}"
my_fullname = name.format(first_name, last_name)
my_name_age = name_age.format(my_fullname, age)
# print(full_name)
# print(my_name_age)

# Index Positions with the string format method.

index_format = "{1} {0}"
my_name_with_index = index_format.format(first_name, last_name)
# print(my_name_with_index)

# Python f-Strings.
# Using python fstrings comes with a lot of advantages like function calls and expressions inside the
# curly brackets.
# Example.

my_name = input("Enter your name:")
f_strings = f"{my_name} {10+9}"
print(f_strings)
# Another Example.
f"{len(name)} {age}"
