import pandas as pd

data = {
    "Name" : ["Ravi", "Aman", "Bhuvan", "Manish"],
    "Age" : [10, 20, 30, 40]
}

df = pd.DataFrame(data)

df.sort_values(by=["Age", "Name"], ascending=(True, False), inplace=True)
print(df)