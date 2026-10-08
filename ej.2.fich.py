#Pedir cinco frases
print("Debes escribir cinco frases ")
Frases = []
for i in range (0,5):
    Frases.append(input("Escribe una frase: "))
#Crear fichero y añadir frases
ruta = "ejercicio2.txt"
with open(ruta,mode = "w", encoding = "utf-8") as fichero:
    for i in Frases:
        print(i, file=fichero)

