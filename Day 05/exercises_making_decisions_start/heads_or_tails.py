import random

guess = input("Guess the coin flip! Enter heads or tails (h/t): ").lower()
guess_number = -1
if guess == "h":
    guess_number = 0
elif guess == "t":
    guess_number = 1

flip = random.randint(0,1)
coin_side = "heads" if flip == 0 else "tails"
result = "correct" if flip == guess_number else "wrong"

print(f"The coin flip was: {coin_side}")
print(f"you guessed {result}!")