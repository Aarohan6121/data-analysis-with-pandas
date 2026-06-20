import pandas as pd

# Loading the data.csv and indexing based on name
df = pd.read_csv("databases/data.csv", index_col="Name")

# Ask the user for a pokemon's name
pokemon = input("Enter a pokemon: ").capitalize()

try:
    # If the user gives a name inside data.csv, this code runs
    print(df.loc[pokemon])
except KeyError:
    # If the user doesnt give a name inside data.csv, this code runs
    print(f"{pokemon} not found!")