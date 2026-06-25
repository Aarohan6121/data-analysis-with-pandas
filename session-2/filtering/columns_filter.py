import pandas as pd

data = {
    "Name" : ["Ram", "Hari", "Shyam", "Bhuvan", "Ashish"],
    "Age" : [28, 31, 35, 32, 29],
    "Salary" : [20000, 30000, 40000, 50000, 60000],
    "Company" : ["Google", "Microsoft", "InfoSys", "Meta", "Twitter"],
    "Performance Score" : [8.0, 7.4, 9.8, 6.8, 9.9]
}

df = pd.DataFrame(data)
# Collecting Company names
companies = df["Company"]
print(companies)

# Collecting Name and Age columns
name_age = df[["Name", "Age"]]
print(name_age)