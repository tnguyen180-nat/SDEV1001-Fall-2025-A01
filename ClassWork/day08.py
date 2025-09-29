user_input = input("Enter the name of a fruit: ")

match user_input:
    case "kamquat":
        print("Where do kamquats come from?")
    case "durian" | "rotten" | "shoe":
        print("Keep your distance.")
    case "starfruit":
        print("What is a starfruit? What Mario eats?")
    case _:
        print("Yah baaaasic!")