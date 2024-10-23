x1 = int(input("Ingresa el valor de x1: "))
y1 = int(input("Ingresa el valor de y1: "))
x2 = int(input("Ingresa el valor de x2: "))
y2 = int(input("Ingresa el valor de y2: "))

distancia = ((x2 - x1)*2 + (y2 - y1)*2) ** 0.5
print("La distancia entre los puntos es:", int(distancia))