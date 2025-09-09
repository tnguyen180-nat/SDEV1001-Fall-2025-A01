COOKIES_PER_BAG = 40
SERVINGS_PER_BAG = 10
CALORIES_PER_SERVING = 300

# Prompt the user to input 
calories_per_cookie = CALORIES_PER_SERVING / (COOKIES_PER_BAG / SERVINGS_PER_BAG)
cookies = int(input("How many cookies did you eat? "))

calories_consumed = cookies * calories_per_cookie

print(f"You ate {cookies} cookies")
print(f"Which is equal to: {calories_consumed} calories")