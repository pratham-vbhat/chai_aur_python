chai_types = {
    "Masala" : "Spicy",
    "Ginger": "Zesty",
    "Green": "Mild",
}

print(chai_types)

print(chai_types["Masala"])

chai_types["Green"] = "Fresh"
print(chai_types)

for chai in chai_types:
    print(f"{chai} is very {chai_types[chai]}")

for key, values in chai_types.items():
    print(f"{key} is very {values}")

chai_types["Earl Grey"] = "Citrus"

print(chai_types)

for key, values in chai_types.items():
    print(f"{key} is very {values}")

chai_types.pop("Ginger")

chai_types.popitem()

del chai_types["Green"]
chai_types_copy = chai_types.copy()

tea_shops = {
    "chai": {
        "Masala" : "Spicy",
        "Ginger" : "Zesty",
    },
    "Tea" : {
        "Green" : "Fresh",
        "Black" : "Strong"
    },
}

print(tea_shops.get("chai"))

squared_number = {x : x**2 for x in range(6)}

# squared_number.clear() # Use this when you want to clear a dictionary.

keys = ["Masala", "Ginger", "Lemon"]

default_value = "Delious"
new_dict = dict.fromkeys(keys, default_value)

# new_dict = dict.fromkeys(keys, keys)