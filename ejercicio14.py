numero = int(input("Ingresa un número de dos cifras: "))

if 10 <= numero <= 99:
    invertido = (numero % 10) * 10 + (numero // 10)
    print("El número invertido es:", invertido)
else:
    print("Por favor ingresa un número de dos cifras.")