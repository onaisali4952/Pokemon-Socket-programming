class Pokemon:
    def __init__(self, name, level, moves):
        self.name = name
        self.level = level
        self.moves = moves  # Initialize the moves list with the provided moves


class Move:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type


# Example usage
moveset1 = [Move("Tackle", 10, "Normal"), Move("Ember", 15, "Fire")]
moveset2 = [Move("Water Gun", 12, "Water"), Move("Vine Whip", 13, "Grass")]

pikachu = Pokemon("Pikachu", 5, moveset1)
charmander = Pokemon("Charmander", 5, moveset1)
squirtle = Pokemon("Squirtle", 5, moveset2)
bulbasaur = Pokemon("Bulbasaur", 5, moveset2)

# Access and print move names from each Pokémon's moves list
for pokemon in [pikachu, charmander, squirtle, bulbasaur]:
    print(f"{pokemon.name}'s moves:")
    for move in pokemon.moves:
        print(f"- {move.name}")
    print()

response = ""
i = 1
response += f"{i}"
print(response)