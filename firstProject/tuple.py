# The tuple data structure is very very smiliar to the list data structure.
# The only difference is that while lists are changeable, tuples are not.
# Tuples are ordered, indexed, allow duplicates and finally are immutable.
# Tuple representation.
my_tuple = ("garri", "rice", "yam")

# A tuple with only one value is written:
data = (
    "red",
)  # add a comma immediately after the item, else it will be an ordinary str.

# Fetching Items in a tuple.
primary_colors = ("red", "green", "blue")
# print(primary_colors[0])
# print(primary_colors[-1])

# Getting a A Range of Items in a tuple.
colors = ("red", "green", "orange", "blue", "white")
# print(colors[1:4])  # the last index isn't included in the range
# print(colors)
# print(colors[:])  # grabs all the items in a tuple.

# Looping Through A Tuple.
# The two ways we are going to look at looping in a tuple is:
# loop for items in the tuple and how to loop for items and the indexes

# Looping through Items in a tuple.
# tuple_1 = ("garri", "sugar", "milk", "milo")
# for item in tuple_1:
#     print(item)

# Looping through items in a tuple and displaying their index.
# t_tuple = ("garri", "indomie", "tea")
# for item in t_tuple:
#     print(item)
#     print(t_tuple.index(item))

# t_tuple = ("garri", "indomie", "tea")
# print(t_tuple.index("garri")) # this will only work if the index garri does not appear twice. Else it will
# return the first instance of the index

# Another Way of Looping through items in a tuple and displaying their index.
# t_tuple = ("age", "info", "diet", "food")
# for x in range(len(t_tuple)):
#   print(x)  # Gives me the index
#   print(t_tuple[x])  # Gives me the item.

# Mutatating or Changing a tuple.
# Mutating a tuple isn't possible. But there is a work around.
# 1. Create a new list off the tuple.
# 2. Update the new list.
# 3. Create a new tuple off the list.

# Example Code
data = ("red", "green", "orange", "white")
print(data)
a_list = list(data)
print(a_list)
a_list.append("indigo")
# print(a_list)
a_list.insert(1, "purple")
# print(a_list)
a_list.pop(4)
# print(a_list)
a_tuple = tuple(a_list)
# print(a_tuple)


# Checking if an item exists in a tuple.
my_tuple = ("rice", "beans", "garri", "meat", "indomie")
print("garri" in my_tuple)
