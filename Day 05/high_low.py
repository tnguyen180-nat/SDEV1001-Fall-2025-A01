PROGRAM_NAME = "High or Low"

import random

random_number = random.randint(1, 100)

number_picked = input("Enter a number between 1 - 100: ")
number_picked_int = int(number_picked)

if number_picked_int > random_number:
    print("That's too damn high!")
elif number_picked_int < random_number:
    print("Too low!")
else:
    print("You got it!")