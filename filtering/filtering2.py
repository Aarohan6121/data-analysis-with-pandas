import pandas as pd

# loading the data.csv file
df = pd.read_csv("databases/data.csv")

# Filtering all the legendary pokemons
legendary_pokemon = df[df["Legendary"] == 1]
print(legendary_pokemon)

#Filtering all the water pokemons
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)

# Filtering all fire with flying pokemons
ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(ff_pokemon)