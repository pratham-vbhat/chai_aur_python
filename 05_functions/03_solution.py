def multiply(mode, a, b):
    if mode == "Integer":
        result = int(a) * int(b)
    elif mode == "String":
        result = str(a) * int(b)
    
    return result

a= input("Enter either number or String: ")
b = input("Enter a number: ")
mode = input("Enter Integer or String:")

result = multiply(mode, a, b)

print(f"Result of multiply is: {result}")
