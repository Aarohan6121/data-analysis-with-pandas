import pandas as pd

data = {
    "Name" : ["Ravi", "Aman", "Bhuvan", "Manish"],
    "Age" : [10, 20, 30, 40],
    "Salary" : [10000, 20000, 30000, 40000]
}

df = pd.DataFrame(data)

# Printing average salary
avg_salary = df["Salary"].mean()
print(avg_salary)

# Printing sum of all the ages
sum_ages = df["Age"].sum()
print(sum_ages)