"""
programa2:
    crear un programa que cxalcule area y perimetro
    de un rectangulo
entradas:
    base: integer
    altura: integer
salidas:
    area: integer
    perimetro: integer

"""

base = input('Ingresa la base: ')
base = int(base)
altura = input('Ingresa la altura: ')
altura = int(altura)
area = base * altura
perimetro = (base + altura) * 2
print("El area del restangulo es", area)
print("El perimetro del rectangulo es:", area)