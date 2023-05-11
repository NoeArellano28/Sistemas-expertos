import random
import os
# Definimos las listas de personajes, lugares y armas
personajes = ["Scarlett", "Mustard", "White", "Green", "Peacock"]
lugares = ["Casa", "Hotel", "Cocina", "Biblioteca", "Jardin"]
armas = ["Cuchillo", "Pistola", "Candelabro", "Llave inglesa", "Cuerda"]

# Definimos las historias y las soluciones correspondientes 
historias = [
    {
        "culpable": "Scarlett",
        "lugar": "Casa",
        "arma": "Cuchillo",
        "historia": "El/La Sr(a).------ ha matado a su esposo en -----. Podras descubrir la verdad?"
    },
    {
        "culpable": "Mustard",
        "lugar": "Hotel",
        "arma": "Pistola",
        "historia": "El/La Sr(a). ----- ha matado al dueno del hotel con ------. Podras encontrar al asesino?"
    },
    {
        "culpable": "White",
        "lugar": "Cocina",
        "arma": "Candelabro",
        "historia": "El/La Sr(a). ---- ha matado al chef en la ------ . Podras resolver el caso?"
    },
    {
        "culpable": "Green",
        "lugar": "Biblioteca",
        "arma": "Llave inglesa",
        "historia": "El/La Sr(a). ------ ha matado al bibliotecario en ------. Podras descubrir la verdad?"
    },
    {
        "culpable": "Peacock",
        "lugar": "Jardin",
        "arma": "Cuerda",
        "historia": "El/La Sr(a).----- ha matado a su vecina en el -----. Podras resolver el caso?"
    }
]
"""
historias = [
    {
        "culpable": "Scarlett",
        "lugar": "Casa",
        "arma": "Cuchillo",
        "historia": "Scarlett ha matado a su esposo en la casa. Podras descubrir la verdad?"
    },
    {
        "culpable": "Mustard",
        "lugar": "Hotel",
        "arma": "Pistola",
        "historia": "El Sr. Mustard ha matado al dueno del hotel con una pistola. Podras encontrar al asesino?"
    },
    {
        "culpable": "White",
        "lugar": "Cocina",
        "arma": "Candelabro",
        "historia": "La Sra. White ha matado al chef en la cocina del restaurante. Podras resolver el caso?"
    },
    {
        "culpable": "Green",
        "lugar": "Biblioteca",
        "arma": "Llave inglesa",
        "historia": "El Profesor Green ha matado al bibliotecario en la biblioteca. Podras descubrir la verdad?"
    },
    {
        "culpable": "Peacock",
        "lugar": "Jardin",
        "arma": "Cuerda",
        "historia": "La Sra. Peacock ha matado a su vecina en el jardin. Podras resolver el caso?"
    }
]
"""
# Generamos aleatoriamente la solución del caso
#caso = random.choice(historias)
while True:
    # Imprimimos la informacion del caso
    caso = random.choice(historias)
    print("\t\t\tBIENVENIDOS A CLUE!\n\t")
    print("Resuelve el siguiente caso!\n\t")
    print("Por seguro sabemos lo siguiente: \n\n\t\t")
    print("1.- La Sra. Peacock dice que escucha muchas discusiones en la casa de su vecina, la Sra. Scarlett, tambien dice que ella ya no sporta los gritos, esta enfadada\n\t")
    print("2.- El profesor de mecanica, el Sr. Green suele leer mucho, principalmente sobre recetas, ya que, a su Hermana y mesera, la Sra. White, es muy exigente con la comida\n\t")
    print("3.- El Sr. Mustard es policia y es el mejor cliente de la ferreteria de la Sra.Peacock, de hecho vendra de viaje a visitarla unos dias a su ciudad\n\t")
    print("\n\t\t\tSabiendo esto, da enter para continuar con el caso...")
    os.system("Pause")
    os.system("cls")
    print(caso["historia"])
    print("\n\tEl sospechoso es uno de los siguientes personajes:")
    print(personajes)
    print("\n\tEl asesinato fue en alguno de estos lugares:")
    print(lugares)
    print("\n\tEl arma utilizada fue una de las siguientes:")
    print(armas)

    # Definimos la funcion para hacer suposiciones
    def hacer_suposicion():
        sup_culpable = input("Quien crees que es el culpable? ")
        sup_lugar = input("Donde crees que se cometio el crimen? ")
        sup_arma = input("Con que arma crees que se cometio el crimen? ")
        return [sup_culpable, sup_lugar, sup_arma]

    # Definimos la funcion para verificar la suposicion del jugador
    def verificar_suposicion(suposicion):
        global personajes, lugares, armas
        if suposicion[0] != caso["culpable"]:
            personajes.remove(suposicion[0])
        if suposicion[1] != caso["lugar"]:
            lugares.remove(suposicion[1])
        if suposicion[2] != caso["arma"]:
            armas.remove(suposicion[2])

    # Comenzamos el juego
    while True:
   
        # Pedimos una suposicion al jugador
        print("\nHaz una suposicion:")
        suposicion = hacer_suposicion()

        # Verificamos la suposicion del jugador
        verificar_suposicion(suposicion)

        # Revisamos si el jugador ha ganado
        if suposicion[0] == caso["culpable"] and suposicion[1] == caso["lugar"] and suposicion[2] == caso["arma"]:
            print("\n\t\t :) Felicitaciones! Has descubierto al asesino.")
            break

        # Revisamos si el jugador ha perdido
        if not personajes or not lugares or not armas:
            print("Lo siento, has perdido. La solucion era:")
            print("Culpable:", caso["culpable"])
            print("Lugar:", caso["lugar"])
            print("Arma:", caso["arma"])
            break

        # Mostramos las opciones disponibles
        print("\n\t :( No has descubierto al asesino. Las opciones disponibles son:")
        print("Personajes:", personajes)
        print("Lugares:", lugares)
        print("Armas:", armas)
    play_again = input("Quieres jugar de nuevo? (s/n): ")
    if play_again != 's':
        break

print("Gracias por jugar. Hasta la proxima!") 
