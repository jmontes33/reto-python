
# Reto Python

En este repositorio encontrarás un fichero CSV que contiene un listado de 5000 posiciones de varios vehículos. Cada una de las líneas detalla las
coordenadas geográficas, fecha y distancia de esa
posición/matrícula.


## El Reto


- CASO 1. Empezamos por algo fácil: Lee el fichero CSV e imprime cada línea.

- CASO 2. Lee el fichero CSV, convierte cada línea a un JSON e imprímelo.

- CASO 3. Subimos de dificultad: En cada fila se incluye la distancia que el vehículo ha recorrido con respecto a su posición anterior. Calcula el sumatorio de las distancias de cada vehículo, usando el campo "distancia" a partir del formato json. Imprime todos los resultados por consola.
- CASO 4. Esto se complica: Ahora calcula el sumatorio de distancias de cada matrícula, usando las coordenadas geográficas (el cálculo debe hacerse a partir del formato json) e imprime todos los resultados por consola.
- CASO 5. ¿Listo? Escribe un nuevo fichero de texto donde aparezca la fecha de la última posición de cada vehículo en formato (dd/mm/YYY HH:MM:SS) a partir del campo "pos_date". Recuerda, pos_date es unafecha en Tiempo POSIX. Escribe el fichero ordenado por fecha, de la más reciente a la más antigua.
- CASO 6. Ahora Crea un API REST con un método GET del estilo (http://localhost/XXX) dónde XXX es la matrícula de un vehículo. Su resultado debe leerse del fichero del punto anterior y devolver la fecha de última posición de la matrícula indicada
- CASO 7. ¿Te atreves a levantar un contenedor Docker con una base de datos e incluir en ella los datos del fichero del punto 5?

- CASO 8. ¡¡La última!! Haz que el API REST del punto 6 lea de la base de datos del punto 7 en vez del fichero del punto 5.

En este repositorio econtrarás los 8 casos resueltos, y la imagen docker utilizada para el caso 7 es la siguiente: https://hub.docker.com/r/jmontes33/postgresql