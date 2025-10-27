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