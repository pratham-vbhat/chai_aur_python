'''
Question-8: Password Strength Checker
'''

def password_strength_checker(password):
    if len(password) < 6:
        return 'weak'
    elif len(password) <=10:
        return "Medium"
    else:
        return "Strong"
    
user_name = input("Kindly enter your name: ")
password = input(f"{user_name} kindly enter your password: ")

password_check = password_strength_checker(password)

print(f"Hy {user_name}. You entered \"{password}\" as your password and it's \"{password_check}\".")