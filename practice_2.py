import pandas as pd

df = pd.read_csv('reto.csv')

for _, row in df.iterrows():
    data = {
        "Matricula": row["Matricula"],
        "Latitud": row["Latitud"],
        "Longitud": row["Longitud"],
        "Distance": row["Distance"],
        "Pos_date": row["Pos_date"]
    }
    print(data)
