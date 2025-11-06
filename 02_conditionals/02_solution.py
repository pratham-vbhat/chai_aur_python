"""Question-2: Movie Ticket Pricing"""

# def check_age(age):
#     if age < 18:
#         return 8
#     else:
#         return 12


def check_weekday(week, price):
	if week.lower() == "wednesday":
		return price - 2
	return price


user_name = input("Enter the name of the user: ")
user_age = int(input(f"Enter the {user_name}'s age: "))

# Method-1
# ticket_pricek = check_age(user_age)

# Method-2
ticket_price = 12 if user_age >= 18 else 8

day_of_week = input("Which day of the week is today?: ")

check_discounts = check_weekday(day_of_week, ticket_price)

print(
	f"Hy {user_name}, thank you for your ticket purchace!!!. As it is {day_of_week}, your movie ticket price is: ${check_discounts}",
)
