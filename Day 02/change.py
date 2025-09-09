total = float(input("Enter an amount (e.g. 1.41): "))
if (total * 100) % 1 != 0:
    print(f"{total} cannot be actual currency.")
else:
    total = int(total * 100)

    quarters = total // 25
    total = total % 25

    dimes = total // 10
    total = total % 10

    nickels = total // 5
    pennies = total % 5

    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")
