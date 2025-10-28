'''
Question-7: Coffee Customization
'''

def cofee_customize(order_size):
    if order_size.lower() == "l":
        return "Large"
    elif order_size.lower() == "m":
        return "Medium"
    else:
        return "Small"

user_name = input("Enter your name: ")
coffee_name = input(f"{user_name}, kindly enter the cofee name: ")
order_size = input(f"{user_name}, kindly enter the size of the cofee (Large (L), Medium (M), Small (S)): ")

extra_shot = input(f"{user_name}, kindly type \"Yes\" if you need extra shot of Espresso, if not then type \"No\": ")

cofee = cofee_customize(order_size)

if extra_shot.lower() == "yes":
    print(f"Hy {user_name}. You have odered {coffee_name} {cofee} with extra shot of Espresso.  Thank you for your order!")
else:
    print(f"Hy {user_name}. You have odered {coffee_name} {cofee}. Thank you for your order!")