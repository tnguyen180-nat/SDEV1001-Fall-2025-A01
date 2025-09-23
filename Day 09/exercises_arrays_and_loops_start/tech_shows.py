

tech_shows = ["Silicon Valley", "Halt and Catch Fire", "Blackberry", "The Billion Dollar Code", "Mr. Robot", "The IT Crowd", "WeCrashed", "The Social Network", "Severance", "Pirates of Silicon Valley"]

first_item = tech_shows[0]
last_item = tech_shows[-1]
tech_shows[tech_shows.index("WeCrashed")] = "The Dropout"
tech_shows[tech_shows.index("The Social Network")] = "Black Mirror"
sub_tech_shows = tech_shows[3:9]

print(f"The best show is {first_item}")
print(f"The most classic show is {last_item}")
print("The fourth to ninth shows on the list are:")
print(sub_tech_shows)

print("The top five shows are:")
i = 0
while i<5:
    print(f"Ranked {i+1} is: {tech_shows[i]}")
    i += 1