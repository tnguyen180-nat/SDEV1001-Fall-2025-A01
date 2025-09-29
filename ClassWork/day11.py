import random

inventory = ["apple", "android", "pixel", "pixel", "pixel", "orangutans", "nokia", "marmite"]
print(inventory)

# inventory.append("caterpillar")
# print(inventory)

# inventory.insert(0, "Dugtrio")
# print(inventory)

# inventory.sort()
# print(inventory)

# inventory.sort(reverse="true")
# print(inventory)

# random.shuffle(inventory)
# print(inventory)

# second_item = inventory.pop(1)
# print(inventory)
# print(second_item)

# if "marmalade" in inventory:
#     inventory.remove("marmalade")
# print(inventory)

# while "pixel" in inventory:
#     inventory.remove("pixel")
# print(inventory)

# inventory.clear()
# print(inventory)

number_of_items = len(inventory)
print(number_of_items)

if "sock" in inventory:
    item_index = inventory.index("sock")
    print(item_index)

item_count = inventory.count("pixel")
print(item_count)

