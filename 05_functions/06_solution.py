def add(
        a: int,
        b: int,
) -> int:
    return a + b


# Use lambda function

cube = lambda x: x ** 3

result = add(10, 20)

print(f"Add: {result}")
print(f"Cube of 3 is: {cube(3)}")