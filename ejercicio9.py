"""
Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

"""

def calcular_total_pago(total_compra):
    descuento = total_compra * 0.15
    total_a_pagar = total_compra - descuento
    return total_a_pagar

total_compra = int(input("Introduce el total de la compra: "))
total_a_pagar = calcular_total_pago(total_compra)
print(f"Total a pagar después del descuento: {total_a_pagar}")
