from fastapi import FastAPI
import uvicorn
import pandas as pd

app = FastAPI()

last_vehicle_position = "ultima_posicion_vehiculos.txt"

df = pd.read_csv(last_vehicle_position)

@app.get("/{matricula}")
async def get_last_position(matricula: str):
    vehiculo = df[df['Matricula'] == matricula]
    if vehiculo.empty:
        return {"error": "Matricula no encontrada"}
    ultima_posicion = vehiculo['Pos_date'].iloc[0]
    return {"Matricula": matricula, "Ultima_Posicion": ultima_posicion}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
