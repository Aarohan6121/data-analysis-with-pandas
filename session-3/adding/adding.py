import pandas as pd

data = {
    "Name" : ["Ram", "Hari", "Shyam"],
    "Age" : [28, 31, 35],
    "Country" : ["Mumbai", "Guwahati", "Pune"]
}

df = pd.DataFrame(data)

# Inserting a new column
new_column = df["Hobbies"] = ["Coding", "Video Games", "Chess"]

# Printing the new data
print(df)

# Using insert(loc, name, [data])
df.insert(1, "Salary", [80000, 120000, 60000])
print(df)