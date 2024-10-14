"""
EJERCICIO 4
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
"""

numero1_input = input("Introduce el primer número: ")
numero1 = int(numero1_input)
numero2_input = input("Introduce el segundo número: ")
numero2 = int(numero2_input)
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 // numero2 if numero2 != 0 else "Error: División por cero"
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")
