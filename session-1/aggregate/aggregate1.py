import pandas as pd

# Initializing the data
df = pd.read_csv("databases/data.csv")

# Whole database(data.csv)
Mean1 = df.mean(numeric_only=True)
Sum1 = df.sum(numeric_only=True)
Min1 = df.min(numeric_only=True)
Max1 = df.max(numeric_only=True)
Count1 = df.count()

# Single column of data.csv
Mean2 = df["Height"].mean()
Sum2 = df["Height"].sum()
Min2 = df["Height"].min()
Max2 = df["Height"].max()
Count2 = df["Type2"].count()

print(Mean1, Sum1, Min1, Max1, Count1)
print(Mean2, Sum2, Min2, Max2, Count2)