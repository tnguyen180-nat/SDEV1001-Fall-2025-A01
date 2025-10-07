# You are developing the functionality that will calculate the number of steps it takes to travel a certain distance in steps
import math

WALKING_DISTANCE = (1/3)
WALKING_SPEED = (1000/15)

# This in the flow:
# 1. User enters the number of distance to travel in meters
distance_asked = int(input("How far do you need to go, in meters? "))

# 2. User is asked if they want to walk, run, or sprint the distance
move_type = ""
while move_type == "" and not (move_type == "w" or move_type == "r" or move_type == "s"):
    move_input = input("Are you (w)alking, (r)unning, or (s)printing? ")
    if move_input == "":
        continue
    move_type = move_input[0]

# 3. If the user walks, they travel 1 step at a time. If they run they travel 2 steps at a time, if they sprint they travel 3 steps at a time.
step_distance = WALKING_DISTANCE
speed = WALKING_SPEED
if move_type == "r":
    step_distance *= 2
    speed *= 2
elif move_type == "s":
    step_distance *= 3
    speed *= 3
    
# 4. Display the number of steps the user takes to travel the distance and the time it takes.
steps = math.ceil(distance_asked / step_distance)
minutes = distance_asked / speed
print(f"You will need to take {steps} steps for {minutes} minutes to get there.")

# Notes:
# - It takes 3 steps to travel 1 meter.
# - It takes 15 minutes to travel one kilometer at walking pace