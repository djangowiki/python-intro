# while a certain condition is true, always run this block of code.
# the while loop has two components. the condition and the block of code.
# the main difference between the for loop and the while loop is that, for the while loop
# the code stops only when the condition evaluates to false. But in for loops, there is
# a definite number of times the code must run.

# Code example.

counter = 5
while counter > 0:
    print(counter)
    counter -= 1
print("Loop has ended")

counter2 = 8
while counter2 % 2 == 0:
    print(counter2)
    counter2 /= 2
print("Loop has ended")

# For a block of code to be executed in a while loop, the condition has to be true.
