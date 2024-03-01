import pandas as pd
import json
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

df = pd.read_csv("reto.csv")

json_data_list = []
for _, row in df.iterrows():
    json_data = row.to_json()
    json_data_list.append(json.loads(json_data))

sumatorios = {}
for item in json_data_list:
    matricula = item['Matricula']
    lat = item['Latitud']
    lon = item['Longitud']
    distancia = item['Distance']

    if matricula in sumatorios:
        sumatorios[matricula] += distancia
    else:
        sumatorios[matricula] = distancia

for matricula, _ in sumatorios.items():
    total_distance = 0
    last_lat = None
    last_lon = None
    for item in json_data_list:
        if item['Matricula'] == matricula:
            lat = item['Latitud']
            lon = item['Longitud']
            if last_lat is not None and last_lon is not None:
                total_distance += haversine(last_lat, last_lon, lat, lon)
            last_lat = lat
            last_lon = lon
    print(f"Matricula: {matricula}, Sumatorio distancias coordenadas: {total_distance}")
