# Question-4: Reverse a String using a Loop

text: str = input("Enter a string: ")
rev_text: str = ""

# Method-1

for char in text:
    rev_text = char + rev_text

print("Method-1")
print(f'The reverse form of this "{text}" text is: "{rev_text}"')

# Method-2:

for ch in text:
    rev_text += ch[:-1]

print("Method-2")
print(f'The reverse form of this "{text}" text is: "{rev_text}"')
