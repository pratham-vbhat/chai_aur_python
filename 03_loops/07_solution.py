# Question-7: Validate Input

while True:
    number: int = int(input("Enter the number between 1 to 10: "))
    if 1 <= number <= 10:
        print(f"The number you entered is: {number}")
        break
    else:
        print(
            f"Enter the valid number!. You entered {number} is more than 10!",
        )
