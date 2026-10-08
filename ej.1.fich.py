ruta = "ejercicio1.txt"
with open(ruta,mode="r", encoding= "utf-8") as fichero:
    lineas = fichero.readlines()
for i in lineas:
    print(i.strip())
