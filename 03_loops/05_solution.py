# Question-5: Find the first non-repeated character:

text: str = input("Enter the string:")
count = 0

for char in text:
    if text.count(char) == 1:
        print(f"The 1st Non-Repeated character from the input text (\"{text}\") is: {char}")
    else:
        continue