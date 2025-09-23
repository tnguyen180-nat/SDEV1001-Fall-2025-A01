# pokemon = []

pokemon = ["Charmander", "Pidgey", "Squirtle"]
print(pokemon)

pokemon.append("Rattata")
print(pokemon)

battle_pokemon = pokemon[-2]
print(f"Go get 'em, {battle_pokemon}!")

pokemon.insert(1, "Bulbasaur")
print(pokemon)

pokemon[3] = "Wartortle"
# pokemon[3] = pokemon[3].upper()
# print(pokemon)

#start_index:end_index

sub_set_pokemon = pokemon[2:]
print(sub_set_pokemon)

war_index = pokemon.index("Wartortle")
print(war_index)

length = len(pokemon)
print(f"You have {length} pokemon.")
