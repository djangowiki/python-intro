user_grade = int(input("Enter your score from 0 to 100: "))
if user_grade >= 70 and user_grade <= 100:
    print("Your Grade is A")
elif user_grade >= 60 and user_grade <= 69:
    print("Your Grade is B")
elif user_grade >= 50 and user_grade <= 59:
    print("Your Grade is C")
elif user_grade >= 45 and user_grade <= 49:
    print("Your Grade is D")
elif user_grade >= 40 and user_grade <= 44:
    print("Your Grade is E")
elif user_grade >= 0 and user_grade <= 39:
    print("Your Grade is F")
else:
    print("You entered the wrong score, please try again")
