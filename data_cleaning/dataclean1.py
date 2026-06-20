import pandas as pd

#Initializing the data
df = pd.read_csv("databases/data.csv")

# Dropping the columns - Legendary and No
df = df.drop(columns=["Legendary", "No"])
print(df)

# Giving None value to pokemons which do no have Type2
df = df.fillna({"Type2" : "None"})
print(df.to_string())