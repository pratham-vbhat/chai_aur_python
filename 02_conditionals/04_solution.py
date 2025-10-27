'''
Question-4: Fruit Ripness Checker

Green  - Unripe
Yellow - Ripe
Brown  - Overripe
'''

def ripe_checker(ripe):
    if ripe == "Green":
        return "Unripe"
    elif ripe == "Yellow":
        return "Ripe"
    elif ripe == "Brown":
        return "Overripe"
    else:
        return "Invalid Input"

fruit_name = input("Enter the name of the fruit: ")
fruit_color = input("Enter the current color of the fruit: ")

ripeness = ripe_checker(fruit_color)

print(f"Your {fruit_name} furit is {fruit_color} in color. So it's {ripeness}.")