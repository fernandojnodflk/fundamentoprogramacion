"""
EJERCICIO 7

Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
"""

minutos_input = input("Introduce la cantidad de minutos: ")
minutos = int(minutos_input)
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")
