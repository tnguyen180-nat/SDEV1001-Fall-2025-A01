# weapons = ["shotgun", "knife", "sword", "BB gun", "water gun"]

# # guns = []
# # for weapon in weapons:
# #     if "gun" in weapon:
# #         guns.append(weapon)
# guns = [weapon for weapon in weapons if "gun" in weapon]

# print(guns) # "['shotgun', 'BB gun', 'water gun']"

# # --------------------------------
# my_string = "Snakes are cool"
# new_string = ""
# vowels = "aeiou"

# for ch in my_string:
#     if not ch in vowels:
#         new_string += ch

# print(new_string)   # Snks r cl

# # --------------------------------
# available_liquids = ["acid", "water", "soda", "bleach", "liquid nitrogen"]
 
# # This is an unchangeable list* of liquids that are safe to drink.
# # *known as a tuple
# drinkable_liquids = ("water", "vinegar", "coffee", "soda")  

# for liquid in available_liquids:
#     if liquid in drinkable_liquids:
#         print(f"You can drink {liquid}!")
#     else:
#         print(f"You can drink {liquid}, but you probably shouldn't...")

# print("Your available liquids:")
# for index, liquid in enumerate(available_liquids):
#     print(f"{index}, {liquid}")

# # --------------------------------
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if (num % 2) == 0 :
#         continue
#     print(f"{num} is odd.")

# # --------------------------------
# animals = ["dog", "cat", "goose", "hamster"]
# for animal in animals:
#     if animal == "goose":
#         print(f"It's a {animal}!  Run away!")
#         break
#     print(f"What a cute {animal}")

# # What a cute dog
# # What a cute cat
# # It's a goose!  Run away!

# # --------------------------------
# user_playing = True
# while user_playing:
#     print("Pew pew!")
#     keep_playing = input("Keep playing (y/n)? ")
#     if keep_playing == "n":
#         user_playing = false

# --------------------------------
while True:
    print("Pew pew!")
    keep_playing = input("Keep playing (y/n)? ")
    if keep_playing == "n":
        break
