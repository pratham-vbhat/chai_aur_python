"""
Question-4: Fruit Ripness Checker

Green  - Unripe
Yellow - Ripe
Brown  - Overripe
"""


def ripe_checker(fruit, ripe):
    if ripe.lower() == "green":
        return "Unripe"
    elif ripe.lower() == "yellow" or ripe.lower() == "red":
        return "Ripe"
    elif ripe.lower() == "brown":
        return "Overripe"
    else:
        return "Invalid Input"


information_list = ["banana", "apple"]

fruit_name = input("Enter the name of the fruit: ")
fruit_color = input("Enter the current color of the fruit: ")

if fruit_name in information_list:
    ripeness = ripe_checker(fruit_name, fruit_color)
    print(f"Your {fruit_name} furit is {fruit_color} in color. So it's {ripeness}.")
else:
    print(
        f"Sorry I currently do not have any information on {fruit_name} fruit!!!. Thank you for your time."
    )
