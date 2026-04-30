import numpy as np

lista_comum = [1, 2, 3, 4, 5]

array_numpy = np.array(lista_comum)

print(array_numpy)
print(type(array_numpy))


lista_multiplicada = [x * 2 for x in lista_comum]
print(lista_multiplicada)
