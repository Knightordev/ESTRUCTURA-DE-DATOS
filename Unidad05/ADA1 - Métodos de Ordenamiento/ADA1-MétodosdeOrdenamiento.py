def ordenamiento_burbuja(lista):
    """Método de ordenamiento burbuja"""
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenamiento_insercion(lista):
    """Método de ordenamiento por inserción"""
    for i in range(1, len(lista)):
        elemento_actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > elemento_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento_actual
    return lista

def ordenamiento_seleccion(lista):
    """Método de ordenamiento por selección"""
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("     SISTEMA DE ORDENAMIENTO")
    print("=" * 50)
    print("1. Ordenamiento Burbuja")
    print("2. Ordenamiento por Inserción")
    print("3. Ordenamiento por Selección")
    print("4. Comparar los 3 métodos")
    print("5. Salir")
    print("=" * 50)

def ingresar_datos():
    """Permite al usuario ingresar datos"""
    print("\n¿Cómo deseas ingresar los datos?")
    print("1. Ingresar manualmente")
    print("2. Usar datos de ejemplo")
    
    opcion = input("\nElige una opción (1-2): ")
    
    if opcion == "1":
        entrada = input("\nIngresa los números separados por comas: ")
        try:
            lista = [float(x.strip()) for x in entrada.split(",")]
            return lista
        except:
            print("Error en el formato. Usando datos de ejemplo.")
            return [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
    else:
        return [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]

def ejecutar_ordenamiento(metodo, lista):
    """Ejecuta el método de ordenamiento seleccionado"""
    lista_copia = lista.copy()
    
    if metodo == 1:
        print("\n--- ORDENAMIENTO BURBUJA ---")
        resultado = ordenamiento_burbuja(lista_copia)
        print("Método: Compara elementos adyacentes y los intercambia")
    elif metodo == 2:
        print("\n--- ORDENAMIENTO POR INSERCIÓN ---")
        resultado = ordenamiento_insercion(lista_copia)
        print("Método: Inserta cada elemento en su posición correcta")
    elif metodo == 3:
        print("\n--- ORDENAMIENTO POR SELECCIÓN ---")
        resultado = ordenamiento_seleccion(lista_copia)
        print("Método: Selecciona el mínimo y lo coloca al inicio")
    
    return resultado

def comparar_metodos(lista):
    """Compara los 3 métodos de ordenamiento"""
    print("\n" + "=" * 50)
    print("     COMPARACIÓN DE LOS 3 MÉTODOS")
    print("=" * 50)
    
    print(f"\nLista original: {lista}")
    
    # Burbuja
    print("\n1. BURBUJA:")
    resultado1 = ordenamiento_burbuja(lista.copy())
    print(f"   Resultado: {resultado1}")
    
    # Inserción
    print("\n2. INSERCIÓN:")
    resultado2 = ordenamiento_insercion(lista.copy())
    print(f"   Resultado: {resultado2}")
    
    # Selección
    print("\n3. SELECCIÓN:")
    resultado3 = ordenamiento_seleccion(lista.copy())
    print(f"   Resultado: {resultado3}")
    
    print("\n✓ Los 3 métodos producen el mismo resultado ordenado")

def main():
    """Función principal del programa"""
    lista_actual = None
    
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "5":
            print("\n¡Gracias por usar el sistema de ordenamiento!")
            print("¡Hasta pronto!")
            break
        
        elif opcion in ["1", "2", "3"]:
            # Ingresar o usar datos actuales
            if lista_actual is None:
                lista_actual = ingresar_datos()
            else:
                usar_actual = input("\n¿Usar la lista actual? (s/n): ")
                if usar_actual.lower() != "s":
                    lista_actual = ingresar_datos()
            
            print(f"\nLista original: {lista_actual}")
            
            # Ejecutar ordenamiento
            resultado = ejecutar_ordenamiento(int(opcion), lista_actual)
            print(f"Lista ordenada: {resultado}")
            
            # Mostrar estadísticas
            print(f"\nEstadísticas:")
            print(f"  - Cantidad de elementos: {len(resultado)}")
            print(f"  - Valor mínimo: {resultado[0]}")
            print(f"  - Valor máximo: {resultado[-1]}")
            print(f"  - Promedio: {sum(resultado) / len(resultado):.2f}")
        
        elif opcion == "4":
            # Comparar los 3 métodos
            if lista_actual is None:
                lista_actual = ingresar_datos()
            else:
                usar_actual = input("\n¿Usar la lista actual? (s/n): ")
                if usar_actual.lower() != "s":
                    lista_actual = ingresar_datos()
            
            comparar_metodos(lista_actual)
        
        else:
            print("\n❌ Opción inválida. Intenta de nuevo.")
        
        input("\nPresiona ENTER para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()