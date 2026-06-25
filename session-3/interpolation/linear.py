import pandas as pd

data = {
    "Time" : [1, 2, 3, 4, 5],
    "Value" : [10, 20, None, None, 50]
}

df = pd.DataFrame(data)

df["Value"] = df["Value"].interpolate(method="linear")
print(df)