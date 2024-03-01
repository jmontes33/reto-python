import pandas as pd
import json

df = pd.read_csv("reto.csv")

json_data_list = []
for _, row in df.iterrows():
    json_data = row.to_json()
    json_data_list.append(json.loads(json_data))

sumatorios = {}
for item in json_data_list:
    matricula = item['Matricula']
    distancia = item['Distance']

    if matricula in sumatorios:
        sumatorios[matricula] += distancia
    else:
        sumatorios[matricula] = distancia

for matricula, sumatoria in sumatorios.items():
    print(f"Matricula: {matricula}, Sumatorio distancias: {sumatoria}")
