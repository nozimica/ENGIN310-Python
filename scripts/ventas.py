# -*- coding: utf-8 -*-
# porcentajes de descuento
dcto2 = 0.1
dcto3 = 0.2
# margen de ganancia
margen = 1.4

# precio1: int -> float
# Dado el costo, calcula el precio de venta
# sin descuento.
# Ejemplo: precio1(2390)
def precio1(costo):
    return round(costo * margen)

# precio2: int -> float
# Dado el costo, calcula el precio de venta
# con descuento por dos tarros.
# Ejemplo: precio2(2390)
def precio2(costo):
    return round(costo * margen * (1 - dcto2))

# precio3: int -> float
# Dado el costo, calcula el precio de venta
# con descuento por tres o más tarros.
# Ejemplo: precio3(2390)
def precio3(costo):
    return round(costo * margen * (1 - dcto3))

# precioTarros: int int -> float
# Dado el costo y la cantidad a vender,
# calcula el valor unitario de cada tarro.
# Ejemplo: precioTarros(2390, 5)
def precioTarros(costo, cantidad):
    if cantidad == 1:
        precio = precio1(costo)
    elif cantidad == 2:
        precio = precio2(costo)
    elif cantidad >= 3:
        precio = precio3(costo)
    else:
        precio = -1
    return precio

# calculaGanancia: int int int int -> float
# Dado el costo y las cantidades vendidas:
# a precio sin descuento (v1)
# con descuento por dos unidades (v2)
# con descuento por tres o más unidades (v3)
# calcula la ganancia total obtenida por todas
# esas ventas.
# Ejemplo: calculaGanancia(2390, 12, 26, 13)
def calculaGanancia(costo, v1, v2, v3):
    precioC1 = precio1(costo)
    precioC2 = precio2(costo)
    precioC3 = precio3(costo)

    gananciaC1 = (precioC1 - costo) * v1
    gananciaC2 = (precioC2 - costo) * v2
    gananciaC3 = (precioC3 - costo) * v3

    return gananciaC1 + gananciaC2 + gananciaC3
