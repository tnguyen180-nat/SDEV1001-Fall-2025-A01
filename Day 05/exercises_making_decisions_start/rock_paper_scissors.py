import random
const HAND = ["scissor", "rock", "paper"]

your_throw = input("Scissor (0), rock (1), paper (2): ")
your_number = int(your_throw)
your_throw = HAND[your_number]

comp_number = random.randint(0,2)
comp_throw = HAND[comp_number]

if your_number == comp_number:
    result = "It is a draw"
elif (your_number - 1) == comp_number or (your_number == 0 and comp_number == 2):
    result = "You win"
else:
    result = "You lose"

print(f"The computer is {comp_throw}. You are {your_throw}. {result}")
