ZODIAC = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey", "rooster", "dog", "pig"]

year_text = input("Enter a year: ")
year_number = int(year_text)

if year_number > 1900: 
    zodiac_index = (year_number - 1900) % 12
else: 
    zodiac_index = (1900 - year_number) % 12

print(ZODIAC[zodiac_index])