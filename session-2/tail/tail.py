import pandas as pd

df = pd.read_json("databases/sample_data.json")

# Printing last 10 rows
print(df.tail(10))