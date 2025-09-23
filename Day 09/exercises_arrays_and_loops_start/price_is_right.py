import random

prices = []
i = 0
while i<3:
    prices.append(random.randint(1,10))
    i += 1

print("Welcome to the Price is Right! Guess the price of this coffee")
user_guess = int(input("Guess the price of the item: "))

if prices[0] == user_guess or prices[1] == user_guess or prices[2] == user_guess:
    print("You win!")
else:
    print("You lose!")
print("The price were:")
print(prices)