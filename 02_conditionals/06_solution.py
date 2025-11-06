"""Question-6: Transport Mode Seletction:
"""


def select_transport_mode(distance):
    if distance < 3:
        return "walk"
    if 3 <= distance < 15:
        return "take bike"
    return "take car"


user_name = input("Enter your name: ")
distance = int(input("Kindly enter the distance you want to travel: "))

mode = select_transport_mode(distance)

print(f"Hy {user_name}. So to travel {distance} Km, you could {mode}")
