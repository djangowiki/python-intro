# Find the maximum number in a non empty list given as [5, 7,12,9,-5,10]
number_list = [5, 7, 12, 9, -5, 10]
print(max(number_list))

# Another method.
number_list2 = [5, 7, 12, 9, -5, 10]
maxNumber = number_list2[0]
for numberItem in number_list2:
    if numberItem > maxNumber:
        maxNumber = numberItem
print(maxNumber)

# Another Method.
number_list3 = [5, 7, 12, 9, -5, 10]
# sort the list.
number_list3.sort()  # it sorts the list in an ascending order. Automatically,
# I can assume that the last item is the largest.
print(number_list3[-1])
