import pandas as pd

data = {
    "Name" : ["Ram", "Hari", "Shyam", "Bhuvan", "Ashish"],
    "Age" : [28, 31, 35, 32, 29],
    "Salary" : [20000, 30000, 40000, 50000, 60000],
    "Company" : ["Google", "Microsoft", "InfoSys", "Meta", "Twitter"],
    "Performance Score" : [8.0, 7.4, 9.8, 6.8, 9.9]
}

df = pd.DataFrame(data)

# Collecting high salary employees
high_salary = df[df["Salary"] >= 40000]
print(high_salary)

# Collecting high performance scores with ages greater than 30
custom = df[(df["Age"] >= 30) & (df["Performance Score"] > 9.0)]
print(custom)