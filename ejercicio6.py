"""
EJERCICIO 6

Calcular la media de tres números pedidos por teclado
"""

num1_input = input("Introduce el primer número: ")
num1 = int(num1_input)
num2_input = input("Introduce el segundo número: ")
num2 = int(num2_input)
num3_input = input("Introduce el tercer número: ")
num3 = int(num3_input)
media = (num1 + num2 + num3) // 3
print(f"La media es: {media}")
