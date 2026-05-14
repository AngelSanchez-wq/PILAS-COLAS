from collections import deque

archivos = deque(["Documento1.pdf", "Imagen.png", "Tarea.docx", "HojaCalculo.xlsx", "Nota.txt"])

print(f"Cola de impresión: {list(archivos)}")

# Imprimir (atender) 3 archivos
for _ in range(3):
    impreso = archivos.popleft()
    print(f"Imprimiendo: {impreso}")

print(f"Documentos pendientes: {list(archivos)}")