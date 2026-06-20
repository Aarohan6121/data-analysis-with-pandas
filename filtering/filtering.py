import pandas as pd

# loading the data.csv file
df = pd.read_csv("databases/data.csv")

# Filtering all the tall pokemons
tall_pokemon = df[df["Height"] >= 3]
print(tall_pokemon)

# Filtering all the heavy pokemons
heavy_pokemon = df[df["Weight"] >= 200]
print(heavy_pokemon)