# Simulación de "Deshacer" con una pila

# Creamos la pila vacía
pila = []

# Función para registrar una acción
def hacer_accion(accion):
    pila.append(accion)
    print(f"Acción realizada: {accion}")

# Función para deshacer la última acción
def deshacer():
    if len(pila) == 0:
        print("No hay acciones para deshacer")
    else:
        accion = pila.pop()
        print(f"Deshacer: {accion}")

# Ejemplo de uso
hacer_accion("Escribió 'Hola'")
hacer_accion("Agregó ' mundo'")
hacer_accion("Borró 'o'")

print("\n--- Estado de la pila ---")
print(pila)

print("\n--- Deshacer acciones ---")
deshacer()
deshacer()
deshacer()
deshacer()  # Aquí ya no habrá nada que deshacer
