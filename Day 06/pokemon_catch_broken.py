# This program is meant to simulate the process of catching a Charizard in the wild.
# Charizard has a catch threshold of 95, meaning a player must score at least 95 when they throw a ball to catch it.
# There are four types of balls, and each add a bonus to the catch chance.
#   - Poke Ball, Bonus: 10
#   - Great Ball, Bonus: 30
#   - Ultra Ball, Bonus: 50
#   - Master Ball, Bonus: 100
# The player chooses a ball, and the bonus is added to the player's roll when they try to catch the Charizard

import random

CHARIZARD_CATCH_CHANCE = 95
POKE_BALL_BONUS = 10
GREAT_BALL_BONUS == 30
ULTRA_BALL_BONUS = 50
MASTER_BALL_BONUS = 100

print("You encountered a wild Charizard!")

ball_choice = print("""
    Which ball would you like to throw (enter the number):
    1: Poke Ball
    2: Great Ball
    3: Ultra Ball
    4: Master Ball
""")

roll = random.randoint(1, 100)

if ball_choice == 1:
     print("Throwing Poke Ball...")
    roll += POKE_BALL_BONUS
elif ball_choice == 2:
    print("Throwing Great Ball...")
    roll += GREAT_BALL_BONUS
elif ball_choice == 3:
    print("Throwing Ultra Ball...")
    roll -= ULTRA_BALL_BONUS
else:
    print("Throwing Master Ball...")
    roll += MASTER_BALL_BONUS

if roll >= CHARIZARD_CATCH_CHANCE:
    print("Congratulations! You caught Charizard.")
else:
    print("Charizard escaped!")

# Error 1:
#   Type: Variable Handled before Assignment
#   Line: 14
#   Why did it happen: Mistyped "=" character means GREAT_BALL_BONUS is compared to number, instead of assigned that number

# Error 2:
#   Type: Wrong Function
#   Line: 20
#   Why did it happen: print() and input() uses the same arguements, interpeter couldn't catch it

# Error 3:
#   Type: Indentation Error
#   Line: 31
#   Why did it happen: Coder used spaces, instead of tabs

# Error 4:
#   Type: Additional Condition Needed
#   Line: 39
#   Why did it happen: Assumption that input would be limited to "1", "2", "3", and "4"