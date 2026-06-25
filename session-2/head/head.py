import pandas as pd

df = pd.read_json("databases/sample_data.json")

# Printing first 10 rows
print(df.head(10))