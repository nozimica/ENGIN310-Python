# -*- coding: cp1252 -*-

# creo un arreglo vacío
valores = []

# le solicito números al usuario
num = raw_input('Ingrese un número ("" para terminar): ')

# mientras no me entregue un ""
while num != "":
    # lo recibido lo convierto a número y lo agrego al arreglo
    valores = valores + [float(num)]
    # vuelvo a solicitar números al usuario
    num = raw_input('Ingrese un número ("" para terminar): ')

# después de que recibí "", aplico la función que calcula la desviación estándar
print("Los valores son:")
print(valores)
print("La desviación estándar es:")
calcularDesvEst(valores)
