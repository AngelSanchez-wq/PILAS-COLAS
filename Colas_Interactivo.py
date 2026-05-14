from collections import deque
cola_usuario = deque()

while True:
    print("\n1. Agregar cliente\n2. Atender cliente\n3. Mostrar cola\n4. Salir")
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        cola_usuario.append(nombre)
    elif opcion == "2":
        if cola_usuario:
            print(f"Atendiendo a: {cola_usuario.popleft()}")
        else:
            print("No hay clientes")
    elif opcion == "3":
        print(f"Cola: {list(cola_usuario)}")
    elif opcion == "4":
        break