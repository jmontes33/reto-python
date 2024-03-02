import pandas as pd
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

sumatorios = {}
coordenadas = {}

for _, row in df.iterrows():
    matricula = row['Matricula']
    lat = row['Latitud']
    lon = row['Longitud']

    if matricula in coordenadas:
        last_lat, last_lon = coordenadas[matricula]
        distancia = haversine(last_lat, last_lon, lat, lon)

        if matricula in sumatorios:
            sumatorios[matricula] += distancia
        else:
            sumatorios[matricula] = distancia

    coordenadas[matricula] = (lat, lon)

for matricula, total_distance in sumatorios.items():
    print(f"Matricula: {matricula}, Sumatorio distancias coordenadas: {total_distance}")
