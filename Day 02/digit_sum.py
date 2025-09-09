number = int(input("Enter an integer between 0 and 1000: "))

if number < 0 or number > 1000:
    print("Not between 0 and 1000.")
else:
    hundreds = number // 100
    tens = (number % 100) // 10
    ones = number % 10
    total = ones + tens + hundreds

    print(f"Sum of digits: {total}")