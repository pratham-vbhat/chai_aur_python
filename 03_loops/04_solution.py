# Question-4: Reverse a String using a Loop

text: str = input("Enter a string: ")
rev_text: str = ''

for char in text:
    rev_text  = char + rev_text

print(f"The reverse form of this \"{text}\" text is: \"{rev_text}\"")
