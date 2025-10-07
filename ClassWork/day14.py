print("Gold Score Calculator")
game_count = 0
score = 0

while True:
    score += int(input("What was your score? "))
    game_count += 1

    keep_playing = input("Want to keep playing (y/n)? ")
    if keep_playing != "y":
        break
    
average = score / game_count
print(f"Your average score is {average}")