import pandas as pd

data = {
    "Name" : ["Ram", None, "Shyam"],
    "Age" : [28, None, 35],
    "Country" : ["Mumbai", None, "Pune"]
}

df = pd.DataFrame(data)

# Detecting None values in the data
print(df.isnull().sum())

# Dropping None values
df.dropna(inplace=True)
print(df)