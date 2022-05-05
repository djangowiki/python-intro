my_food_item_list = ["garri", "peak milk", "bournvita", "biscuits", "peak milk"]
# print(my_food_item_list)

# We access the list of an item in python using index. And we have two types of indexes.
# The positive index and the negative index.
# print(my_food_item_list[0])  # positive indexing
# print(my_food_item_list[-5])  # negative indexing

# Range of indexes in a python lists
list_items = my_food_item_list[2:4]
# print(list_items)

# Updating or changing list values.
my_food_item_list[2] = "milo"
# print(my_food_item_list)

# Python List Loop
for i in range(5):
    print(my_food_item_list[i])

# Better way to write Python List Loop
# for item in range(len(my_food_item_list)):
#     print(my_food_item_list[item])

# Shorter better method for writing Python List Loop
for item in my_food_item_list:
    print(item)
