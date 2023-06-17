import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "musica22",
    database = "autos"
)
c = conn.cursor()

# Comprobar si la conexión se realizó exitosamente
if conn:
    print("Conexion exitosa a la base de datos.")
else:
    print("Error al conectar a la base de datos.")

# Obtener recomendaciones de automóviles según las necesidades del cliente
def obtener_recomendaciones(presupuesto, marca, edad, estado_civil, tiene_hijos):
    recomendaciones = []

    if estado_civil == "Soltero":
        # Si el cliente es soltero, se recomienda un auto deportivo
        c.execute("SELECT * FROM autos WHERE tipo_carroceria = 'Deportivo' AND precio <= %s AND marca = %s ORDER BY precio ASC", (presupuesto, marca))
        recomendaciones += c.fetchall()
    elif estado_civil == "Casado" and tiene_hijos:
        # Si el cliente está casado y tiene hijos, se recomienda una SUV
        c.execute("SELECT * FROM autos WHERE tipo_carroceria = 'SUV' AND precio <= %s AND marca = %s ORDER BY precio ASC", (presupuesto, marca))
        recomendaciones += c.fetchall()
    else:
        # Para otros casos, se recomienda un sedán
        c.execute("SELECT * FROM autos WHERE tipo_carroceria = 'Sedan' AND precio <= %s AND marca = %s ORDER BY precio ASC", (presupuesto, marca))
        recomendaciones += c.fetchall()

    # Filtrar recomendaciones basadas en la edad
    if edad < 25:
        # Si el cliente es menor de 25 años, se eliminan las SUV de las recomendaciones
        recomendaciones = [auto for auto in recomendaciones if auto[4] != "SUV"]
    elif edad > 50:
        # Si el cliente es mayor de 50 años, se eliminan los deportivos de las recomendaciones
        recomendaciones = [auto for auto in recomendaciones if auto[4] != "Deportivo"]

    return recomendaciones

# Interfaz de usuario
def interfaz_usuario():
    print("Bienvenido al sistema de recomendacion de autos!")
    print("Por favor, ingrese la siguiente informacion:")
    
    presupuesto = float(input("Presupuesto maximo: "))
    marca = input("Marca deseada: ")
    edad = int(input("Edad del cliente: "))
    estado_civil = input("Estado civil (Soltero/Casado): ")
    tiene_hijos = input("Tiene hijos? (Si/No): ").lower() == "si"
    
    # Obtener recomendaciones
    recomendaciones = obtener_recomendaciones(presupuesto, marca, edad, estado_civil, tiene_hijos)
    
    # Mostrar las recomendaciones
    print("Aqui esta la mejor opcion para ti!")
    print("-----******------*****-----*****-----")
    for auto in recomendaciones:
        print(f"Modelo: {auto[1]}")
        print(f"Marca: {auto[2]}")
        print(f"Precio: ${auto[3]}")
        print(f"Tipo de carroceria: {auto[4]}")
        print("-----------")
    
    # Cerrar la conexión a la base de datos
    conn.close()

# Ejecutar la interfaz de usuario
interfaz_usuario()

