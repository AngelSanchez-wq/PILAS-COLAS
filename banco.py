from collections import deque

cola = deque()

cola.append('Ana')
cola.append('Carlos')
cola.append('Luisa')
cola.append('Pedro')

print("Fila actual:")
for cliente in cola:
    print(cliente)

cliente_atendido = cola.popleft()
print(f"\nAtendiendo: {cliente_atendido}")

cliente_atendido = cola.popleft()
print(f"Atendiendo: {cliente_atendido}")


print(f"\nSiguiente cliente:")
print(cola[0])