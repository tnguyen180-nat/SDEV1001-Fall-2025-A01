concert_name = input("What is the name of the concert tonight? ")
has_ticket = input("Do you have a ticket (y/n)? ").lower()

if has_ticket == "y":
    if concert_name == "taylor swift":
        print("you're in the right place")
        print("have fun!")
    elif concert_name == "billie eilish":
        print("this concert is next door") 
    if concert_name == "Guns n Roses":
        print("Yaay!")
    elif concert_name == "Wind Rose":
        print("Black riders! Run!")
    elif concert_name == "Falconer":
        print("Ve are svedish. Ve like saunas!")
    else:
        print("this is not the concert you are looking for")
else:
    print("No ticket? Buzz off!")