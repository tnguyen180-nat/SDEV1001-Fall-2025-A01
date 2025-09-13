year_text = input("Enter a year: ")
year_number = int(year_text)

answer = "false"
if (year_number % 4 == 0 and year_number % 100 != 0) or year_number % 400 == 0:
    answer = "true"

print(f"Is {year_text} a leap year? {answer}")