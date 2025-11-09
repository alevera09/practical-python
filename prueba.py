import time

for i in range(101):
    print(f"Progreso: {i}%", end="\r") # \r mueve el cursor al inicio
    time.sleep(0.05) # Pequeña pausa para ver el efecto
print("\n¡Completado!")
