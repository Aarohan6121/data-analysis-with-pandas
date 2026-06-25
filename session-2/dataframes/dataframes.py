import pandas as pd

data = {
    "Name" : ["Ram", "Hari", "Shyam"],
    "Age" : [28, 31, 35],
    "Country" : ["Mumbai", "Guwahati", "Pune"]
}

df = pd.DataFrame(data)

# Printing the dataframe
print(df)

# Moving the data to json file
df.to_json("dataframes/database.json", index=False)

# Moving the data to csv file
df.to_csv("dataframes/database.csv", index=False)