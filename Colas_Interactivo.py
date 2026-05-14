from collections import deque

# Inicializamos la cola para gestionar clientes del banco
cola_usuario = deque()

while True:
    print("\n1. Agregar cliente\n2. Atender cliente\n3. Mostrar cola\n4. Salir")
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        # Agregamos al final de la fila
        nombre = input("Nombre: ")
        cola_usuario.append(nombre)
    elif opcion == "2":
        # Desencolar: Verificamos si hay clientes antes de intentar atender
        if cola_usuario:
            # Atendemos al que lleva más tiempo esperando
            print(f"Atendiendo a: {cola_usuario.popleft()}")
        else:
            # Validación para evitar errores si la cola está vacía
            print("No hay clientes")
    elif opcion == "3":
        # Visualización del estado actual de la estructura
        print(f"Cola: {list(cola_usuario)}")
    elif opcion == "4":
        # Rompemos el ciclo infinito para cerrar el programa
        break