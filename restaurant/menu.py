import json
from modules import *


with open("menu.json", "r") as f:
    data = json.load(f)

items = data.get("items", [])


line()
print("Welcome to Nandos")
line()

while True:
    print("<1> Menu Maintenance")
    print("<2> Order Food")
    print("<3> Check Order")
    print("<4> Payment")
    print("<5> Sales Reports")
    print("<Q>uit")
    line()
    choice = int(input("Enter option >> "))
    print("")

    if choice == 1:
        food_name = input("Enter item name >> ")
        price = input("Enter item price >> ")
        food_type = input("Veg / Non-veg >> ")
        items.append(
            {
                "id": len(items) + 1,
                "name": food_name,
                "price": price,
                "veg": True if food_type == "Non-veg" else False,
                "reviews": [],
            }
        )

        data["items"] = items
        with open("menu.json", "w") as f:
            json.dump(data, f)
            print("item has been added")
