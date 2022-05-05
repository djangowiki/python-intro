# In a given list, there is always one largest element. Find whether the largest element
# in the list is at least twice as much as every other number in the list.
# If it is, print the index of the largest element, otherwise print -1.

# Method 1.
number_list = [3, 6, 1, 0]
max_number = number_list[0]
max_number_index = 0
counter = 0

for i in range(len(number_list)):
    if number_list[i] > max_number:
        max_number = number_list[i]
        max_number_index = i
for number in number_list:
    if max_number == number:
        continue
    if max_number >= 2 * number:
        counter += 1
if counter == len(number_list) - 1:
    print(max_number_index)
else:
    print(-1)

# Method 2.
number_list2 = [3, 6, 1, 0]
max_number2 = max(number_list2)
max_number2_index = 0
counter2 = 0
for num in range(len(number_list2)):
    if max_number2 == number_list2[num]:
        max_number2_index = num
for item in number_list2:
    if max_number2 == item:
        continue
    if max_number2 > 2 * item:
        counter2 += 1
if counter == len(number_list2) - 1:
    print(max_number2_index)
else:
    print(-1)
