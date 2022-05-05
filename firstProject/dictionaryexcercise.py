# Given a list of integers, determine the number of occurences of each item,
# in the list and print out the item and each occurence.
# Example, given a list [2, 2, 3,5,2,3,1,0,5].
# print
# 2 3
# 3 2
# 5 2
# 1 1
# 0 1

list_of_integers = [2, 2, 3, 5, 2, 3, 1, 0, 5]
dictionary = {}

for value in list_of_integers:
    if value in dictionary:
        count = dictionary[value]
    else:
        count = 0
    dictionary[value] = count + 1

for key, value in dictionary.items():
    print(key, value)
