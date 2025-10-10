# You are developing the functionality that will calculate the number of steps it takes to travel a certain distance in steps
import math

STEPS_PER_METRE = 3
WALKING_SPEED = (1000/15)

# This in the flow:
# 1. User enters the number of distance to travel in meters
distance_asked = int(input("How far do you need to go, in meters? "))

# 2. User is asked if they want to walk, run, or sprint the distance
move_type = ""
while move_type == "" and not (move_type == "w" or move_type == "r" or move_type == "s"):
    move_input = input("Will you (w)alk, (r)un, or (s)print? ")
    if move_input == "":
        continue
    move_type = move_input[0]

# 3. If the user walks, they travel 1 step at a time. If they run they travel 2 steps at a time, if they sprint they travel 3 steps at a time.
match move_type:
    case "w":
        steps_per_step = 1
    case "r":
        steps_per_step = 2
    case "s":
        steps_per_step = 3
    
# 4. Display the number of steps the user takes to travel the distance and the time it takes.
steps = math.ceil((distance_asked * STEPS_PER_METRE) / steps_per_step)
time = distance_asked / (WALKING_SPEED * steps_per_step)
print(f"You will need to take {steps} steps for {time} minutes to travel {distance_asked} metres.")

# Notes:
# - It takes 3 steps to travel 1 meter.
# - It takes 15 minutes to travel one kilometer at walking pace