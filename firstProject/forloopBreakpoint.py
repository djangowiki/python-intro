# What if you want to break out of the loop even when all the conditions are still true.
# Because, we established that we can only breakout of the forloop when the condition is false.
# This is how to break out of the forloop according to our own requirement.
# The break statement terminates all the loops.

for i in range(10):
    if i == 5:
        break
    print(i)
