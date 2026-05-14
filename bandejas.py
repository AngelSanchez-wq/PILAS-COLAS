# Pila de Bandejas
bandejas = []

# Agregar 5 bandejas
colores = ["Roja", "Azul", "Verde", "Amarilla", "Blanca"]
for color in colores:
    bandejas.append(color)

print("Pila inicial:", bandejas)

# Retirar las dos últimas
bandejas.pop()
bandejas.pop()

print("Pila final:", bandejas)