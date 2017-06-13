# -*- coding: cp1252 -*-

# cerca: num num num -> bool
# Retorna True si la diferencia entre x e y es menor a epsilon.
# Ejemplo: cerca(0.33333, 1/3.0, 0.001) retorna True
def cerca(x, y, epsilon):
    diff = x - y
    return abs(diff) < epsilon

# heronRaizRec: num num num -> num
# Calcula la raíz cuadrada de x con una precisión epsilon,
# y un valor inicial de la estimación.
# Ejemplo: heronRaizRec(13, 0.001, 13/2.0) retorna 3.6055512902583184
def heronRaizRec(x, epsilon, estimacion):
    if cerca(estimacion**2, x, epsilon):  # caso base
        return estimacion
    else:                                 # caso recursivo
        nuevaEstimacion = (estimacion + (x / estimacion)) / 2.0
        return heronRaizRec(x, epsilon, nuevaEstimacion)

# heronRaiz: num num -> num
# Calcula la raíz cuadrada de x con una precisión epsilon.
# Ejemplo: heronRaiz(13, 0.001) retorna 3.6055512902583184
def heronRaiz(x, epsilon):
    return heronRaizRec(x, epsilon, x/2.0)

# Probamos la función con la verdadera sqrt
import math
assert cerca(heronRaiz(3, 0.001), math.sqrt(3), 0.001)
assert cerca(heronRaiz(5, 0.001), math.sqrt(5), 0.001)
assert cerca(heronRaiz(11, 0.001), math.sqrt(11), 0.001)
