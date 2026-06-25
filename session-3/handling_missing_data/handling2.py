import pandas as pd

data = {
    "Name" : ["Ram", None, "Shyam"],
    "Age" : [28, None, 35],
    "Country" : ["Mumbai", None, "Pune"]
}

df = pd.DataFrame(data)

# Filling None values
df["Age"].fillna(df["Age"].mean(), inplace=True)