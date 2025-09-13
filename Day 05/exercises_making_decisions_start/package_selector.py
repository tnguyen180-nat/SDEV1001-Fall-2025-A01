print("Welcome to the Ultimate Gym\n")
print("Please select a membership package: \n\
- Package A: $40/month, 4 months (short-term package)\n \
- Package B: $55/month, 8 months (standard package)\n \
- Package C: $75/month, 12 months (regular package)\n \
- Package D: $100/month, 12 month (premium package, includes 4 free personal training sessions)\n \
\n\
\n\
")

selection = input("Enter the package letter (A/B/C/D): ").upper()
match selection:
    case "A":
        fee = 40
        months = 4
    case "B":
        fee = 55
        months = 8
    case "C":
        fee = 75
        months = 12
    case "D":
        fee = 100
        months = 12
    case _:
        fee = 0
        months = 0
cost = fee * months

print(f"You have selected Package {selection}")
print(f"Your monthly fee is ${fee}\n\
Your total fee is ${cost}")