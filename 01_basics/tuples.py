tea_types = ("Black", "Green", "Oolong")

print(tea_types[0])
# tea_types[0] = "Lemmon" # You cannot assign extra items to Tupes once created. Throws an error.
more_teas = ("Hearbal", "Earl Grey", "Lemon")

all_tea = more_teas + tea_types

if "Green" in more_teas:
    print("I have Green Tea")
else:
    print("I dont have the Tea requested!!!")

(black, green, oolong) = more_teas
