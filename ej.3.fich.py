# Leer el contenido del fichero frases.txt y mostrarlo por pantalla
ruta = "frases.txt"
print("Contenido actual de frases.txt:")
with open(ruta, mode="r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
for i in lineas:
    print(i.strip())

# Pedir cinco frases más al usuario
print("\nDebes escribir cinco frases más")
Frases = []
for i in range(0, 5):
    Frases.append(input("Escribe una frase: "))

# Añadir las nuevas frases a las ya existentes
with open(ruta, mode="a", encoding="utf-8") as fichero:
    for i in Frases:
        print(i, file=fichero)

