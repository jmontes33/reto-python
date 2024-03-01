from fastapi import FastAPI
from fastapi.responses import JSONResponse
import psycopg2

app = FastAPI()

conn_params = {
    "host": "localhost",
    "port": "5433",
    "database": "postgres",
    "user": "postgres",
    "password": "Abc123.",
}

def get_last_position_from_db(matricula):
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        cursor.execute("SELECT Pos_date FROM vehiculos WHERE Matricula = %s;", (matricula,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None

    except psycopg2.Error as e:
        return str(e)

    finally:
        if conn:
            cursor.close()
            conn.close()

@app.get("/{matricula}")
async def get_last_position(matricula: str):
    ultima_posicion = get_last_position_from_db(matricula)
    if ultima_posicion is not None:
        return JSONResponse(content={"Matricula": matricula, "Ultima_Posicion": ultima_posicion})
    else:
        return JSONResponse(content={"error": "Matricula no encontrada"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
