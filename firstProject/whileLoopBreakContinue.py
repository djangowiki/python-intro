counter = 8
while counter > 0:
    if counter == 4:
        counter -= 1
        break

    print(counter)
    counter -= 1
print("Loop ends here.")

counter2 = 8
while counter2 > 0:
    if counter2 == 4:
        counter2 -= 1
        continue
    print(counter2)
    counter2 -= 1
print("Loop ends here")
