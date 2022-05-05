# print out the highest number in this set.
a_set = {5, 20, 70, 46, 50}
highest_num = 0
for item in a_set:
    if item > highest_num:
        highest_num = item
print(highest_num)
