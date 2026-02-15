# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 10:46:29 2026

@author: ASUS VIVOBOOK
"""

# Juego: La computadora adivina el número del usuario

print("Piensa en un número entre 1 y 100.")
print("La computadora intentará adivinarlo.")

# Definimos los límites iniciales
minimo = 1
maximo = 100

# Variable de control del bucle
adivinado = False

# Contador de intentos
intentos = 0

while not adivinado:
    # La computadora calcula un número intermedio
    intento = (minimo + maximo) // 2
    intentos += 1

    print(f"\n¿Tu número es {intento}?")
    respuesta = input("Escribe 'mayor', 'menor' o 'correcto': ").lower()

    if respuesta == "mayor":
        # Ajustamos el límite inferior
        minimo = intento + 1

    elif respuesta == "menor":
        # Ajustamos el límite superior
        maximo = intento - 1

    elif respuesta == "correcto":
        adivinado = True
        print(f"\n¡La computadora adivinó tu número en {intentos} intentos!")

    else:
        print("Respuesta no válida. Intenta de nuevo.")