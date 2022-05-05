# There are two types of if else in python.
# 1. Inclusive if else where the conditions will intersect and the order you write
# the if else matters.
# 2. Exclusive if else where the conditions does not intersect and the order you
# write the if else does not matter.

# Example of Inclusive if else is the code below.
# To write inclusive if else, we have to start it at the point of the overlap.
# At the point of the intersection.
user_number = int(input("Enter a Number: "))
if user_number % 2 == 0 and user_number % 3 == 0:
    print("Your number is a multiple of 2 and 3")
elif user_number % 2 == 0:
    print("Your number is a multiple of 2")
elif user_number % 3 == 0:
    print("Your number is a multiple of 3")
else:
    print("Something went wrong, please try again")
