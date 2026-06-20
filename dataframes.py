import pandas as pd

# Initializing the data
data = {
    "Name" : ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30, 35, 50]
}

df = pd.DataFrame(data)

# Add a new column
df["Job"] = ["Cook", "Receptionist", "Cashier"]

# Create and append new user record
new_row = pd.DataFrame([{"Name" : "Sandy", "Age" : 40, "Job" : "Manager"}], index=[4])
new_df = pd.concat([df, new_row])

# Printing the new dataframe
print(new_df)