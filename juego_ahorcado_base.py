
# Juego que simula el ahorcado.
# Puedes cometer 6 fallos
# Importaciones
# ----------------------------------------------------------
import random
from os import system, name

# Constantes
# ----------------------------------------------------------
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

# Funciones
# ----------------------------------------------------------
def clear(): 
  
    # Para windows 
    if name == 'nt': 
        _ = system('cls') 
    # Para mac y linux(aquí, os.name es 'posix') 
    else: 
        _ = system('clear') 

def elijeLetra(letrasUtilizadas): 
    # Devuelve la letra que el jugador introdujo. Esta función hace que el jugador introduzca una letra y no cualquier otra cosa 
    while True: 
        print ('Adivina una letra:') 
        letra = input() 
        letra = letra.lower() 
        if len(letra) != 1: 
            print ('Introduce una sola letra.') 
        elif letra in letrasUtilizadas: 
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?') 
        elif letra not in 'abcdefghijklmnñopqrstuvwxyz': 
            print ('Elije una letra y no otro símbolo.') 
        else: 
            return letra 

# Variables
# ----------------------------------------------------------
lista_palabras = ["casa","techo","ropa","gato","perro","hoja","carta"]
# Programa Principal
# ----------------------------------------------------------
# Elegir la palabra a adivinar
palabra = lista_palabras[random.randint(0,len(lista_palabras)-1)]
letras_falladas = ""
# Mostrar HUD y guiones
guiones = "_" * len(palabra)
print(AHORCADO[0])
# Mientras no se gane o pierda
while len(letras_falladas) < 6 and guiones != palabra :
    print(guiones)
    # Pedir letra
    letra = input("Dime una letra: ")
    # Comprobar si está en la palabra o no
    if letra not in palabra: 
        letras_falladas = letras_falladas + letra
    else:   
        indice = 0
        for i in palabra:
            if i == letra:
                guiones = guiones[:indice] + letra + guiones[indice+1:]
            indice = indice + 1
    print("Letras acertadas: " , guiones)
    print("Letras falladas: " , letras_falladas)
    print(AHORCADO[len(letras_falladas)])
#Comprobar si se ha ganado o perdido
if len(letras_falladas) == 6 :
    print("Has perdido, la palabra secreta era ",palabra)
else:
    print("¡Felicidades, has ganado!")















