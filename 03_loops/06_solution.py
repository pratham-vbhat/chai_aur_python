# Question-6: Factorial Number

num: int = int(input("Enter the factorial number: "))
factorial: int = 1
factorial_number: int = num

while num > 0:
    if num == 0 and num == 1:
        factorial = 1
    else:
        factorial *= num
        num -= 1

print(
    f'Factorial of a number ("{factorial_number}") is: {factorial}',
)
