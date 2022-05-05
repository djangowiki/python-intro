import random

# One time part.
random_number = random.randint(0, 20)
# print(random_number) spoiling the fun of the game.
guess_number = int(input("Enter a Guess Number: "))

# Repetitive parts
while guess_number != random_number:
    if guess_number > random_number:
        print("Your guess is greater than the random number")
    else:
        print("Your guess is less than the random number")
    guess_number = int(input("Enter a Guess Number: "))
print("You guessed right!")
