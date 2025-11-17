# Qustion-8: Prime Number Checher

num: int = int(input("Enter a number: "))

isPrime: bool = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            isPrime = False
        else:
            isPrime = True

print(
    f"The Number you entered {num} is (Prime means True and Not Prime is False): {isPrime}",
)
