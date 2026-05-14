pila = []

while True:
    # Mostrar menú
    print("\n--- MENÚ PILA ---")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Mostrar pila")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        elemento = input("¿Qué elemento quieres agregar? ")
        pila.append(elemento)
        print(f"'{elemento}' agregado a la pila.")

    elif opcion == "2":
        if len(pila) == 0:
            print("La pila está vacía, no hay nada que eliminar.")
        else:
            eliminado = pila.pop()
            print(f"'{eliminado}' eliminado de la pila.")

    elif opcion == "3":
        if len(pila) == 0:
            print("La pila está vacía.")
        else:
            print("Pila actual:")
            print(pila)

    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Elige entre 1 y 4.")