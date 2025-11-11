# Question-5: Multiplication Table Printer


mul_num: int = int(input("Which multiplication table do you wanna seee?: "))

print(f"Multiplication Table of {mul_num}:")

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(f"{mul_num} x {i} = {mul_num * i}")
