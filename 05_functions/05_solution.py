def greet(
        name: str = "User",
) -> None:
    print(f"Hi {name},\n\tGood Morning!")


name = input("Enter your name: ")
greet(name)
greet("Pratham")
