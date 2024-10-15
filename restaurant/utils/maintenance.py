import json


def menu_maintenance():
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
