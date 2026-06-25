import pandas as pd

df = pd.read_json("databases/sample_data.json")

# Printing the info of the file
print(df.info())