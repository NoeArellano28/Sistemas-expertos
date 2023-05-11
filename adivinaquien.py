import mysql.connector

# establecer la conexion a la base de datos MySQL
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="musica22",
  database="base"
)

cursor = conexion.cursor()
cursor.execute("SELECT nombre, pelota, equipo, campo, agua, invierno FROM deportes")
#global deportes 
#deportes = [row for row in cursor.fetchall()]



def jugar_adivina_el_deporte():
    conexion = mysql.connector.connect(
    host="localhost",
       user="root",
       password="musica22",
       database="base"
    )

    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, pelota, equipo, campo, agua, invierno FROM deportes")
    global deportes 
    deportes = [row for row in cursor.fetchall()]
    # jugar "Adivina el deporte"
    print("Bienvenido a Adivina el deporte")
    print("Piensa en un deporte y responde las preguntas con 's' para si y 'n' para no")
    
    # definir las preguntas
    preguntas = [
      "Se requiere una pelota para jugar?",
      "Se juega en equipo?",
      "Se juega en un campo?",
      "Se juega en el agua?",
      "Se juega sobre hielo?"
    ]

    # hacer todas las preguntas y guardar las respuestas en una lista
    respuestas = []
    for pregunta in preguntas:
      respuesta = input(pregunta + " (s/n) ")
      respuestas.append(respuesta)
    # funcion para filtrar la lista de deportes basandose en la respuesta a la pregunta actual
    def filtrar_deportes(deportes, pregunta, respuesta):
      indice_pregunta = preguntas.index(pregunta)
      if respuesta == "s":
        return [deporte for deporte in deportes if deporte[indice_pregunta+1]]
      else:
        return [deporte for deporte in deportes if not deporte[indice_pregunta+1]]
    
    # filtrar la lista de deportes basandose en las respuestas dadas
    for respuesta, pregunta in zip(respuestas, preguntas):
      deportes = filtrar_deportes(deportes, pregunta, respuesta)

    # adivinar el deporte restante
    if len(deportes) == 1:
      print("El deporte que pensaste es", deportes[0][0], "!")
    else:
      print("No conozco ese deporte")




# funcion para imprimir el menu y obtener la opcion elegida por el usuario
def obtener_opcion():
  print("----- Menu -----")
  print("1. Jugar Adivina el deporte")
  print("2. Agregar un nuevo deporte")
  print("3. Salir")
  opcion = input("Ingrese el numero de la opcion que desea: ")
  return opcion




def agregar_nuevo_deporte():
  conexion = mysql.connector.connect(
  host="localhost",
    user="root",
    password="musica22",
    database="base"
    )

  cursor = conexion.cursor()
  #cursor.execute("SELECT nombre, pelota, equipo, campo, agua, invierno FROM deportes")
  print("Agregar un nuevo deporte")
  print("(Selecciona (0) para NO y (1) para SI)")
  nombre = input("Ingrese el nombre del deporte: ")
  pelota = input("Se requiere una pelota para jugar? (0/1): ")
  equipo = input("Se juega en equipo? (0/1): ")
  campo = input("Se juega en un campo? (0/1): ")
  agua = input("Se juega en el agua? (0/1): ")
  invierno = input("Se juega sobre hielo? (0/1): ")
  cursor.execute(f"INSERT INTO deportes (nombre, pelota, equipo, campo, agua, invierno) VALUES ('{nombre}', '{pelota}', '{equipo}', '{campo}', '{agua}', '{invierno}')")
  conexion.commit()
  print("Deporte agregado con exito") 


opcion = obtener_opcion()
while opcion != "3":
  
  if opcion == "1":
    jugar_adivina_el_deporte()
  elif opcion == "2":
    agregar_nuevo_deporte() 
  else:
    print("Opcion no valida") 


