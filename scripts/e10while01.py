# -*- coding: cp1252 -*-

# creo un arreglo vac�o
valores = []

# le solicito n�meros al usuario
num = raw_input('Ingrese un n�mero ("" para terminar): ')

# mientras no me entregue un ""
while num != "":
    # lo recibido lo convierto a n�mero y lo agrego al arreglo
    valores = valores + [float(num)]
    # vuelvo a solicitar n�meros al usuario
    num = raw_input('Ingrese un n�mero ("" para terminar): ')

# despu�s de que recib� "", aplico la funci�n que calcula la desviaci�n est�ndar
print("Los valores son:")
print(valores)
print("La desviaci�n est�ndar es:")
calcularDesvEst(valores)
