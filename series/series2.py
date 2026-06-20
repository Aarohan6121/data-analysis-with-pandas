import pandas as pd

# Initializing the data
calories = {
    "Day 1" : 1750,
    "Day 2" : 2150,
    "Day 3" : 1550
}

series = pd.Series(calories)

# Filter criteria: Numbers >= 2000
print("\nCalories which are >= 2000:")
print(series[series >= 2000])