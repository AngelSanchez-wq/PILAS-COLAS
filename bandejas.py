# Pila de Bandejas
bandejas = []

# Agregamos elementos al final de la lista
colores = ["Roja", "Azul", "Verde", "Amarilla", "Blanca"]
for color in colores:
    bandejas.append(color) # append() coloca el elemento arriba de los demás

print("Pila inicial:", bandejas)

# Eliminamos los últimos elementos agregados (LIFO: El último en entrar es el primero en salir)
# pop() sin argumentos siempre elimina y retorna el elemento de la cima
bandejas.pop() # Elimina blanca
bandejas.pop() # Elimina amarilla

# El estado final muestra que solo quedan los primeros elementos agregados
print("Pila final:", bandejas)