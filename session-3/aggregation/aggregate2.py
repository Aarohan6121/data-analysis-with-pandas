import pandas as pd

data = {
    "Name" : ["Ravi", "Aman", "Bhuvan", "Manish"],
    "Age" : [10, 10, 20, 30],
    "Salary" : [10000, 20000, 30000, 40000]
}

df = pd.DataFrame(data)

# Grouping salary with age
grouped_data = df.groupby("Age")["Salary"].sum()
print(grouped_data)