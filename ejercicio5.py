"""
EJERCICIO 5

Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
"""


fahrenheit_input = input("Introduce la temperatura en grados Fahrenheit: ")
fahrenheit = int(fahrenheit_input)  
celsius = (fahrenheit - 32) * 5 // 9
print(f"Temperatura en grados Celsius: {celsius}")
