"""
8.- Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
 y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

"""

def calcular_total_vendedor(sueldo_base, ventas):
    comisiones = sum(ventas) * 0.10
    total_recibido = sueldo_base + comisiones
    return comisiones, total_recibido

sueldo_base = 1000
ventas = [200, 300, 500]
comisiones, total_recibido = calcular_total_vendedor(sueldo_base, ventas)
print(f"Comisiones: {comisiones}")
print(f"Total recibido en el mes: {total_recibido}")
