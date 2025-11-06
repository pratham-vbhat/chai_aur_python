"""Question-1: Age Group Categoritaion."""


from typing import Literal


def check_age(age) -> None | Literal["Child"] | Literal["Teenager"] | Literal["Adult"] | Literal["Senior Citizen"]:
    if age < 13:
        return "Child"
    if 13 < age < 19:
        return "Teenager"
    if 20 < age < 59:
        return "Adult"
    if age > 60:
        return "Senior Citizen"
    return None


user_name = input("Enter the person's name: ")
user_age = int(input(f"Enter the {user_name}'s age: "))

age_check = check_age(user_age)

print(
    f"According to the age of {user_name} his/her age is {user_age} and he/she is an {age_check}",
)
