# Historial del Navegador usando Pila (Stack)

# 1. Crear una pila vacía
historial = []

# 2. Agregar 4 páginas web
historial.append('Google')
historial.append('YouTube')
historial.append('Classroom')
historial.append('GitHub')

# 3. Mostrar el historial completo
print("Historial:")
print(historial)

# 4. Eliminar las últimas 2 páginas visitadas
pagina_cerrada = historial.pop()
print(f"\nSe cerró: {pagina_cerrada}")

pagina_cerrada = historial.pop()
print(f"Se cerró: {pagina_cerrada}")

# 5. Mostrar cuál página queda abierta al final
print(f"\nPágina actual:")
print(historial[-1])