import pandas as pd

csv_file = 'reto.csv'

data = []

df = pd.read_csv(csv_file)

df['Pos_date'] = pd.to_datetime(df['Pos_date'], unit='ms', errors='coerce')

df = df.sort_values(by='Pos_date', ascending=False)

df_last_positions = df.groupby('Matricula').first().reset_index()

df_last_positions['Pos_date'] = df_last_positions['Pos_date'].dt.strftime('%d/%m/%Y %H:%M:%S')

df_last_positions.to_csv('ultima_posicion_vehiculos.txt', index=False, columns=['Matricula', 'Pos_date'])

print("Archivo 'ultima_posicion_vehiculos.txt' creado")
