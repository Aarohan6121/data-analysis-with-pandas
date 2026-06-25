import pandas as pd

#Initializing the data
df = pd.read_csv("databases/data.csv")

# Replacing Grass-GRASS, Water-WATER and Fire-FIRE
df["Type1"] = df["Type1"].replace({"Water" : "WATER", "Fire" : "FIRE", "Grass" : "GRASS"})
print(df.to_string())

# Making the names of pokemons in lowercase
df["Name"] = df["Name"].str.lower()
print(df.to_string())
print(df.to_string())

# Drop duplicates in data.csv file
df = df.drop_duplicates()
print(df.to_string())