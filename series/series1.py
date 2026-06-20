import pandas as pd

# Initializing the data
data = [100, 200, 300, 40, 500, 600, 700, 800, 900, 1000]

series = pd.Series(data)

# Printing the number at index no. 5
print(series.iloc[5])

# Filter criteria: Numbers <= 500
print("\nNumbers which are <= 500:")
print(series[series <= 500])