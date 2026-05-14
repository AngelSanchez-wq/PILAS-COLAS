from collections import deque

# Usamos deque porque es más eficiente para eliminar elementos al inicio
archivos = deque(["Documento1.pdf", "Imagen.png", "Tarea.docx", "HojaCalculo.xlsx", "Nota.txt"])

print(f"Cola de impresión: {list(archivos)}")

# Simulamos la impresión de 3 archivos
# FIFO: El primero que llegó a la cola es el primero que se imprime
for _ in range(3):
    # popleft() extrae el elemento que está al frente de la fila
    impreso = archivos.popleft()
    print(f"Imprimiendo: {impreso}")

# Los elementos restantes son los que llegaron de último
print(f"Documentos pendientes: {list(archivos)}")