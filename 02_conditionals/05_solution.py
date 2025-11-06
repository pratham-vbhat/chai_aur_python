"""
Question-5: Weather Activity Suggestion
"""


def weather_activity(weather):
    if weather.lower() == "sunny":
        return "go for a walk"
    elif weather.lower() == "rainy":
        return "read a Book"
    elif weather.lower() == "winter":
        return "build a Snowman"
    else:
        return f"Invalid Weather or currently we do not have any information on the {weather}"


user_name = input("Kindly enter your name: ")
weather = input(f"{user_name}, could you kindly enter the current weather: ")

result = weather_activity(weather)

print(f"Hy {user_name}, the weather outside is {weather}, so you could {result}!!!.")
