from collections import deque

# Creación de la lista enlazada
lista = deque()

# Agregar elementos a la lista
lista.append(["Palabra", "Algo mas"])
print(lista)
lista.append([5, 8])
print(lista)
lista.append([17, 0, 3, 7])
print(lista)
lista.append(["palabra 2"])
print(lista)
lista.append(["palabra 3"])
print(lista)

# Eliminar el último elemento
lista.pop()

# Imprimir el tamaño de la lista
print("El tamaño de la lista es:", len(lista))

# Obtener el último elemento
print(lista[-1])
