import pandas as pd

# Loading the data.csv and indexing based on name
df = pd.read_csv("databases/data.csv", index_col="Name")

# Give information about Pikachu's height and weight
print(df.loc["Pikachu", ["Height", "Weight"]])