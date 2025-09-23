import random

print("You're working at a grocery store and suddenly a zombie bursts through the door looking right at you with hunger in its eyes!")

decision = input("""
    What are you going to do!!!!
    A. Throw a jar of mayonnaise at the zombie.
    B. Sacrifice a customer and run.
    C. Call the manager.
    D. Pull out your pocket shotgun and shoot the zombie.
    E. Take your lunch break.
""").upper()

match decision:
    case "A":
        hit_chance = 8
        roll = random.randint(1, 12)
        if hit_chance >= 8:
            print("You hit the zombie directly in the head with the jar of mayo.")
            print("It is impressed by your accuracy and invites you to join it's baseball team.")
            accept = input("Do you accept? (y/n)")
            print("The zombie charges directly at you. Ya dead!")
    case "B":
        print("You grab a customer and throw it at the zombie.")
        distraction_chance = 5
        grab_customer_chance = 10
        grab_roll = random.randint(1, 12)
        if grab_roll >= grab_customer_chance:
            print("You grab the customer and toss them at the zombie.")
            distraction_roll = random.randint(1, 12)
            if distraction_roll >= distraction_chance:
                print("The zombie attacks the customer and you escape!")
            else:
                print("The zombie is not in the mood for customer and charges at you. Ya dead!")
        else:
            print("The customer grabs you instead and throws you at the zombie. Ya dead!")
    case "C":
        print("You call for the manager, but it turns out THEY are the zombie. Ya dead!")
    case "D":
        print("You pull your pocket shotgun out of your back pocket. This is the moment you have been training for.")
        hit_chance = 2
        hit_roll = random.randint(1, 12)
        if hit_roll >= hit_chance:
            print("Bull's Eye! That zombie didn't know what was coming to it.")
        else:
            print("You miss! All that Call of Duty for nothing! The zombie charges at you. Ya dead!")
    case "E":
        print("It's lunch time. You charge at the zombie.")
        eat_chance = 10
        eat_roll = random.randint(1, 12)
        if eat_roll >= eat_chance:
            print("You eat the zombie. It didn't expect that.")
        else:
            print("The zombie bites back!")
    case _:
        print("The zombie charges directly at you. Ya dead!")

# Error 1:
#   Type: Formatting
#   Line: 12
#   Why did it happen: Wrong function called, match expect uppercase instead of lower

# Error 2:
#   Type: Formatting
#   Line: 39
#   Why did it happen: case "F" should not exist, should be "D"

# Error 3:
#   Type: Formatting
#   Line: 17
#   Why did it happen: Upper bound is too low, will roll will always be less than hit_chance

# Error 4:
#   Type: Formatting
#   Line: 18
#   Why did it happen: condition will not vary, if statment will always pass; recommend comparing between other variables

# Error 5:
#   Type: Formatting
#   Line: 21
#   Why did it happen: No space after asking for input, looks ugly

# Error 6:
#   Type: Formatting
#   Line: 28
#   Why did it happen: condition will not vary, if statment will always fail; recommend comparing between other variables

# Error 7:
#   Type: Formatting
#   Line: 30
#   Why did it happen: Variable for "roll" was assigned to a constant number, not random

# Error 8:
#   Type: TypeError
#   Line: 51
#   Why did it happen: Wrong function called to create one variable; should be int and not bytes
