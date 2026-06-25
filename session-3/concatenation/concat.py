import pandas as pd

df1 = pd.DataFrame({
    "Time" : [1, 2, 3, 4, 5],
    "Values" : [10, 20, 30, 40, 50]
})

df2 = pd.DataFrame({
    "Time" : [6, 7, 8, 9, 10],
    "Values" : [60, 70, 80, 90, 100]
})

concat_df = pd.concat([df1, df2], axis=1, ignore_index=True)
print(concat_df)