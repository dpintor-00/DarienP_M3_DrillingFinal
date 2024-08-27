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

# Clasificación listas magos-cientificos-otros.
# Se utilizan listas vacías y luego mediante un ciclo for se recorre la lista personas para posteriormente agregar a la lista respectiva el nombre en específico que se busca.

magos = []
cientificos = []
otros = []

for mago in personas:
    if mago == "Harry Houdini":
        magos.append(mago)
    elif mago == "David Blaine":
        magos.append(mago)
    elif mago == "Teller":
        magos.append(mago)

for cientifico in personas:
    if cientifico == "Newton":
        cientificos.append(cientifico)
    elif cientifico == "Hawking":
        cientificos.append(cientifico)
    elif cientifico == "Einstein":
        cientificos.append(cientifico)

for otro in personas:
    if otro == "Messi":
        otros.append(otro)
    elif otro == "Pele":
        otros.append(otro)
    elif otro == "Juanes":
        otros.append(otro)

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