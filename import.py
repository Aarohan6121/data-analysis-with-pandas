import pandas as pd

df_csv = pd.read_csv("databases/data.csv")
# df_json = pd.read_json("data.json")

print(df_csv.to_string())
# print(df_json.to_string())