import pandas as pd

data = pd.read_excel('Customer_Profiling.xlsx') 
df = pd.DataFrame(data)
df = df["PARENT'S FULL NAME"].tolist()
for name in df:
    print(name + 'lol')