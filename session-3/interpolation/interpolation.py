import pandas as pd

data = {
    "Name" : ["Ram", "Hari", "Shyam"],
    "Age" : [28, 30, 35],
    "Country" : ["Mumbai", "Guwahati", "Pune"]
}

df = pd.DataFrame(data)

# Interpolating values
df.interpolate(method="linear", axis=0, inplace=True)