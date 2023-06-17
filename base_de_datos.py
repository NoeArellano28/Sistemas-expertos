#import sqlite3

import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "musica22",
    database = "autos"
    )
c = conn.cursor()

# Crear tabla autos
c.execute('''CREATE TABLE IF NOT EXISTS autos (
              id INT auto_increment PRIMARY KEY ,
              modelo varchar(255),
              marca varchar(255),
              precio INT,
              tipo_carroceria varchar(255)) ''')

# Insertar datos de muestra
autos = [
    ("Corolla", "Toyota", 20000, "Sedan"),
    ("Accord", "Honda", 25000, "Sedan"),
    ("Escape", "Ford", 30000, "SUV"),
    ("Trax", "Chevrolet", 35000, "SUV"),
    ("M3", "BMW", 50000, "Deportivo"),
    ("R8", "Audi", 60000, "Deportivo")
]

c.executemany("INSERT INTO autos (modelo, marca, precio, tipo_carroceria) VALUES (%s, %s, %s, %s)", autos )

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()
                

print("Base de datos creada exitosamente.")

