import pandas as pd

data1 = pd.DataFrame({
    "Name" : ["Aarohan", "Bhuvan", "Chirag", "Danish", "George"],
    "Age" : [20, 21, 22, 23, 24]
})

data2 = pd.DataFrame({
    "Name" : ["Harsh", "Jackie", "Messi", "Narendra", "Prutul"],
    "Age" : [25, 26, 27, 28, 29]
})

df_merged = pd.merge(data1, data2, on=["Name", "Age"], how="outer")
print(df_merged)