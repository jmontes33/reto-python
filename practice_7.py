import psycopg2
import pandas as pd
from psycopg2 import sql

conn_params = {
    "host": "localhost",
    "port": "5433",
    "database": "postgres",
    "user": "postgres",
    "password": "Abc123.",
}

df = pd.read_csv("ultima_posicion_vehiculos.txt")

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'vehiculos'
        );
    """)
    table_exists = cursor.fetchone()[0]

    if table_exists:
        create_table_query = '''
        CREATE TABLE vehiculos_temp (
            id SERIAL PRIMARY KEY,
            Matricula VARCHAR(100),
            Pos_date VARCHAR(50)
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()

        for _, row in df.iterrows():
            cursor.execute(
                sql.SQL("INSERT INTO vehiculos_temp (Matricula, Pos_date) VALUES (%s, %s);"),
                (row['Matricula'], row['Pos_date'])
            )
        conn.commit()

        cursor.execute("DROP TABLE vehiculos;")
        conn.commit()

        cursor.execute("ALTER TABLE vehiculos_temp RENAME TO vehiculos;")
        conn.commit()

    else:
        create_table_query = '''
        CREATE TABLE vehiculos (
            id SERIAL PRIMARY KEY,
            Matricula VARCHAR(100),
            Pos_date VARCHAR(50)
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()

        for _, row in df.iterrows():
            cursor.execute(
                sql.SQL("INSERT INTO vehiculos (Matricula, Pos_date) VALUES (%s, %s);"),
                (row['Matricula'], row['Pos_date'])
            )
        conn.commit()

    print("Datos introducidos")

except (Exception, psycopg2.Error) as error:
    print("Error al conectar con la base de datos:", error)

finally:
    if conn:
        cursor.close()
        conn.close()
