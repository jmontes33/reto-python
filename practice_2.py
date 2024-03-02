import pandas as pd

df = pd.read_csv('reto.csv')

for _, row in df.iterrows():
    data = row.to_json()
    print(data)
