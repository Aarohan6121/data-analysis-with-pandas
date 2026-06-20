import pandas as pd

# Initializing the data
df = pd.read_csv("databases/data.csv")

group = df.groupby("Type1")

# Filtering the average of each Type1
print(group["Height"].mean())

# Filtering the min height of each Type1
print(group["Height"].min())

# Filtering the max height of each Type1
print(group["Height"].max())