"""Question-3: Student Grade Calculator
"""


def grade_assigner(grade):
    if 90 <= grade <= 100:
        return "A"
    if 80 <= grade <= 89:
        return "B"
    if 70 <= grade <= 79:
        return "C"
    if 60 <= grade <= 69:
        return "D"
    return "F"


user_name = input("Enter the person's name: ")
user_score = int(input(f"Enter {user_name}'s total score (out of 100): "))

if user_score in range(101):
    grade = grade_assigner(user_score)
    print(
        f"{user_name} has scored {user_score} in his exams and he/she has secured {grade} grade.",
    )
else:
    print("Invalid Score!!. Enter valid score (within 100)")
