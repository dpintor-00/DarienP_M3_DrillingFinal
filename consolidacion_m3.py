# Se define una lista de personas

personas = ["Harry Houdini",
            "Newton",
            "David Blaine",
            "Hawking",
            "Messi",
            "Teller",
            "Einstein",
            "Pele",
            "Juanes"
]

# Clasificación listas magos-cientificos-otros

magos = [personas[0], personas[2], personas[5]]
cientificos = [personas[1], personas[3], personas[6]]
otros = [personas[4], personas[7], personas[8]]

# Se definen funciones, "imprimir_x" imprime las listas de personas antes clasificadas
# "hacer_grandioso" modifica la lista de magos para que antes de cada nombre el string diga "El gran [mago]"

def imprimir_nombres():
    for personas_famosas in personas:
        print(personas_famosas)
    print("\n")

def imprimir_magos():
    for personas_magos in magos:
        print(personas_magos)
    print("\n")

def imprimir_cientificos():
    for personas_de_ciencias in cientificos:
        print (personas_de_ciencias)
    print("\n")

def imprimir_restantes():
    for personas_restantes in otros:
        print(personas_restantes)

def hacer_grandioso():
    for n in range(len(magos)):
        magos[n] = (f"El gran {magos[n]}")

# Desde aquí se imprimen los datos, ejecutando en orden las funciones definidas anteriormente

print("Las siguientes personas han dejado su impronta en distintas áreas, siendo grandes conocidos,")
imprimir_nombres()

# Ejecuta función para que los strings de la lista de magos contengan "El gran" antes del nombre del mago en cuestión
hacer_grandioso()

print("De entre aquellas personas enlistadas se encuentran connotados magos,")
imprimir_magos()

print("También se encuentran los científicos")
imprimir_cientificos()

print("Y personas de otras áreas, como el deporte y la música:")
imprimir_restantes()