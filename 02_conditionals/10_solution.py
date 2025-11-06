"""
Question-10. Pet Food Recommendation
"""


def pet_food_recommend(animal, animal_age):
    if animal.lower() == "dog":
        if animal_age < 2:
            return "So we recommend you to give Puppy Food"
        elif 2 <= animal_age < 7:
            return "So we recommend you to give Senior Dog Food"
        else:
            return "Find a grave for your dog. Thank you!!!"
    elif animal.lower() == "cat":
        if animal_age < 5:
            return "So we recommend you to give Kitten Food"
        elif 5 <= animal_age < 7:
            return "So we recommend you to give Senior Cat Food"
        else:
            return "Find a grave to your cat. Thank you!!!"
    else:
        return "You live with ghost. Die Quickly!!!"


user_name = input("Enter your name: ")
animal = input(f"Hy {user_name}, kindly enter what animal do you have?: ")
animal_age = int(input(f"Hy {user_name}, kindly enter the age of your animal: "))

pet_food = pet_food_recommend(animal, animal_age)

print(
    f"Hy {user_name}, We got to know that you have {animal} as your pet animal. {pet_food}"
)
