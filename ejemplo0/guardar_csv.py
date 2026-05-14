from base_datos import conn
import pandas as pd
cursor = conn.cursor()

df = pd.read_csv('./data/info.csv')
print(df.head())
for index, fila in df.iterrows():
    nombre = fila['nombre']
    apellido = fila['apellido']
    cedula = fila['cedula']
    edad = fila['edad']
    cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) \
    VALUES ('%s', '%s', '%s', %d);""" % (nombre, apellido, cedula, edad)
    # ejecutar el SQL
    cursor.execute(cadena_sql)


# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
