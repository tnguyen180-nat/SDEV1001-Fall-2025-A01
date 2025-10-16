print("Golf Score Calculator")
count = 0
total_score = 0

while True:
    user_input = input("What was your recent golf score? (enter 'quit' to stop) ")
    if user_input == "quit":
        break
    else:
        try:
            total_score += int(user_input)
            count += 1
        except ValueError as error_message:
            print(f"ValueError: {error_message}")

try:
    avg = total_score / count
    print(f"Your average is {avg}!")
except ZeroDivisionError as error_message:
    print(f"Cannot divide by zero. Error: {error_message}")