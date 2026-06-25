import pandas as pd

data = {
    "Name" : ["Ram", "Hari", "Shyam"],
    "Age" : [28, 31, 35],
    "Country" : ["Mumbai", "Guwahati", "Pune"]
}

df = pd.DataFrame(data)

# Using df.drop(columns = ["name"], inplace=True)
df.drop(columns=["Country"], inplace=True)
print(df)