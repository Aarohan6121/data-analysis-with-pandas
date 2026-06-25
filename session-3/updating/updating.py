import pandas as pd

data = {
    "Name" : ["Ram", "Hari", "Shyam"],
    "Age" : [28, 31, 35],
    "Country" : ["Mumbai", "Guwahati", "Pune"]
}

df = pd.DataFrame(data)

# Printing the data
print(df)

# Using df.loc[row_index, "name"] = new_value
df.loc[0, "Age"] = 29

# Making age increase by 5
df["Age"] = df["Age"] + 5

# Printing the new data
print(df)