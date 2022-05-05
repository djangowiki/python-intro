# A set is unordered.
# A set does not allow duplicate values
# A set value cannot be changed but the number of items in the set can be increased or decreased.
# A set is not indexed
# A set can have different data types.

# Code:
# How to create a set in python.
s_set = {1, "eggs", 4}

# Fetching Items from a set
# The only way to fetch items from a set is by using loops.
# Looping Through A set

# for item in s_set:
#     print(item)

# Checking if an item exists in a set.
a_set = {40, True, "Info", "Money", "Mac"}
# print("Mac" in a_set)

# if "Info" in a_set:
#     print("Info can be found in the set: ", a_set)
# else:
#     print("Info cannot be found in the set: ", a_set)

# Adding Item to a set.
# Remember, we can add new items and we can remove an item in a set. But we cant change an item or replace them.
# How to Add item to a set
# We use the add method.
a_set.add("Mango")
# print(a_set)

# Removing item from a set.
# We use the discard() and remove() method.
# When trying to remove an item from a set, it is safe to use the discard method since it doesn't throw
# an error if the item you want to remove does not exists.
# my_set = {True, False, "Mango", "Orange"}
# my_set.discard(True)
# print(my_set)
# my_set.remove("True")
# print(my_set)
# Another method used to remove an item from  set is the pop() method. It does not take any parameter
# With pop, we can't really tell which item got removed. But we can pass it into a variable and print it to know
# for example:
# ss_set = {"mac", "hp", "lenovo", "asus"}
# item = ss_set.pop()
# print(item)
# print(ss_set)
# The advantage of using the pop method is that it returns the item that got removed from the set.
# The clear method is used to clear all the items in a set.
clear_set = {"info", "nft", "data", 2}
print(clear_set)
clear_set.clear()
print(clear_set)
