10
cal1 = int(input("Ingresa la primera calificación parcial: "))
cal2 = int(input("Ingresa la segunda calificación parcial: "))
cal3 = int(input("Ingresa la tercera calificación parcial: "))
examen_final = int(input("Ingresa la calificación del examen final: "))
trabajo_final = int(input("Ingresa la calificación del trabajo final: "))

promedio_parciales = (cal1 + cal2 + cal3) / 3
calificacion_total = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15) 

print("Tu calificación final es:", int(calificacion_total))