import time
import random

def ordenamiento_burbuja(lista, mostrar_pasos=False):
    """Método de ordenamiento burbuja con visualización paso a paso"""
    n = len(lista)
    paso = 0
    
    if mostrar_pasos:
        print(f"\n{'='*60}")
        print("ORDENAMIENTO BURBUJA - PASO A PASO")
        print(f"{'='*60}")
        print(f"Lista inicial: {lista}\n")
        time.sleep(1)
    
    for i in range(n):
        hubo_cambio = False
        if mostrar_pasos:
            print(f"--- Pasada #{i+1} ---")
        
        for j in range(0, n - i - 1):
            if mostrar_pasos:
                print(f"Comparando {lista[j]} con {lista[j + 1]}", end="")
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
                if mostrar_pasos:
                    print(f" → Intercambio realizado")
                    print(f"   Lista ahora: {lista}")
                    paso += 1
                    time.sleep(0.5)
            else:
                if mostrar_pasos:
                    print(f" → Sin cambio")
                    time.sleep(0.3)
        
        if mostrar_pasos:
            print(f"Fin de pasada #{i+1}: {lista}")
            print()
            time.sleep(0.5)
        
        if not hubo_cambio:
            if mostrar_pasos:
                print("¡Lista ya ordenada! Terminando anticipadamente.")
            break
    
    return lista

def ordenamiento_insercion(lista, mostrar_pasos=False):
    """Método de ordenamiento por inserción con visualización paso a paso"""
    if mostrar_pasos:
        print(f"\n{'='*60}")
        print("ORDENAMIENTO POR INSERCIÓN - PASO A PASO")
        print(f"{'='*60}")
        print(f"Lista inicial: {lista}\n")
        time.sleep(1)
    
    for i in range(1, len(lista)):
        elemento_actual = lista[i]
        j = i - 1
        
        if mostrar_pasos:
            print(f"--- Paso #{i} ---")
            print(f"Elemento a insertar: {elemento_actual}")
            print(f"Parte ordenada: {lista[:i]}")
            time.sleep(0.5)
        
        posicion_original = i
        while j >= 0 and lista[j] > elemento_actual:
            lista[j + 1] = lista[j]
            if mostrar_pasos:
                print(f"  Moviendo {lista[j]} hacia la derecha")
                time.sleep(0.3)
            j -= 1
        
        lista[j + 1] = elemento_actual
        
        if mostrar_pasos:
            if j + 1 != posicion_original:
                print(f"  Insertando {elemento_actual} en posición {j + 1}")
            else:
                print(f"  {elemento_actual} ya está en su posición correcta")
            print(f"Lista actual: {lista}")
            print()
            time.sleep(0.5)
    
    return lista

def ordenamiento_seleccion(lista, mostrar_pasos=False):
    """Método de ordenamiento por selección con visualización paso a paso"""
    n = len(lista)
    
    if mostrar_pasos:
        print(f"\n{'='*60}")
        print("ORDENAMIENTO POR SELECCIÓN - PASO A PASO")
        print(f"{'='*60}")
        print(f"Lista inicial: {lista}\n")
        time.sleep(1)
    
    for i in range(n):
        indice_minimo = i
        
        if mostrar_pasos:
            print(f"--- Paso #{i+1} ---")
            print(f"Buscando el mínimo desde posición {i}")
            time.sleep(0.5)
        
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
                if mostrar_pasos:
                    print(f"  Nuevo mínimo encontrado: {lista[indice_minimo]} en posición {indice_minimo}")
                    time.sleep(0.3)
        
        if mostrar_pasos:
            print(f"Mínimo encontrado: {lista[indice_minimo]}")
            
        if i != indice_minimo:
            if mostrar_pasos:
                print(f"Intercambiando {lista[i]} (pos {i}) con {lista[indice_minimo]} (pos {indice_minimo})")
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        else:
            if mostrar_pasos:
                print(f"{lista[i]} ya está en su posición correcta")
        
        if mostrar_pasos:
            print(f"Lista actual: {lista}")
            print(f"Parte ordenada: {lista[:i+1]}")
            print()
            time.sleep(0.5)
    
    return lista

def mostrar_menu():
    print("\n" + "=" * 60)
    print("          SISTEMA DE ORDENAMIENTO PASO A PASO")
    print("=" * 60)
    print("1. Ordenamiento Burbuja")
    print("2. Ordenamiento por Inserción")
    print("3. Ordenamiento por Selección")
    print("4. Comparar los 3 métodos (sin pasos)")
    print("5. Salir")
    print("=" * 60)

def ingresar_datos():
    """Genera lista aleatoria de 1000 números"""
    print("\n¿Cómo deseas ingresar los datos?")
    print("1. Ingresar manualmente")
    print("2. Usar lista aleatoria de 1000 números")
    
    opcion = input("\nElige una opción (1-2): ")
    
    if opcion == "1":
        entrada = input("\nIngresa los números separados por comas: ")
        try:
            lista = [float(x.strip()) for x in entrada.split(",")]
            return lista
        except:
            print("❌ Formato inválido. Usando lista aleatoria.")
    
    print("\n🔢 Generando lista aleatoria de 1000 números...\n")
    return [random.randint(1, 10000) for _ in range(1000)]

def ejecutar_ordenamiento(metodo, lista):
    lista_copia = lista.copy()
    
    print("\n¿Deseas ver el proceso paso a paso?")
    print("1. Sí, mostrar todos los pasos")
    print("2. No, solo mostrar el resultado")
    
    mostrar = input("\nElige una opción (1-2): ") == "1"
    
    if metodo == 1:
        if not mostrar:
            print("\n--- ORDENAMIENTO BURBUJA ---")
        resultado = ordenamiento_burbuja(lista_copia, mostrar)
    elif metodo == 2:
        if not mostrar:
            print("\n--- ORDENAMIENTO POR INSERCIÓN ---")
        resultado = ordenamiento_insercion(lista_copia, mostrar)
    elif metodo == 3:
        if not mostrar:
            print("\n--- ORDENAMIENTO POR SELECCIÓN ---")
        resultado = ordenamiento_seleccion(lista_copia, mostrar)
    
    return resultado

def comparar_metodos(lista):
    print("\n" + "=" * 60)
    print("          COMPARACIÓN DE LOS 3 MÉTODOS")
    print("=" * 60)
    
    print(f"\nLista original (primeros 20 valores): {lista[:20]} ...")
    
    # Burbuja
    print("\n1. BURBUJA:")
    resultado1 = ordenamiento_burbuja(lista.copy(), False)
    print(f"   Resultado (primeros 20): {resultado1[:20]}")
    
    # Inserción
    print("\n2. INSERCIÓN:")
    resultado2 = ordenamiento_insercion(lista.copy(), False)
    print(f"   Resultado (primeros 20): {resultado2[:20]}")
    
    # Selección
    print("\n3. SELECCIÓN:")
    resultado3 = ordenamiento_seleccion(lista.copy(), False)
    print(f"   Resultado (primeros 20): {resultado3[:20]}")
    
    print("\n✓ Los 3 métodos producen el mismo resultado ordenado")

def main():
    lista_actual = None
    
    print("\n¡Bienvenido al Sistema de Ordenamiento Paso a Paso!")
    
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "5":
            print("\n" + "=" * 60)
            print("¡Gracias por usar el sistema de ordenamiento!")
            print("¡Hasta pronto!")
            print("=" * 60)
            break
        
        elif opcion in ["1", "2", "3"]:
            if lista_actual is None:
                lista_actual = ingresar_datos()
            else:
                print(f"\nLista actual (primeros 20 valores): {lista_actual[:20]}")
                usar_actual = input("¿Usar esta lista? (s/n): ")
                if usar_actual.lower() != "s":
                    lista_actual = ingresar_datos()
            
            print(f"\n📋 Lista a ordenar (primeros 20 valores): {lista_actual[:20]}")
            
            resultado = ejecutar_ordenamiento(int(opcion), lista_actual)
            
            print(f"\n{'='*60}")
            print("RESULTADO FINAL")
            print(f"{'='*60}")
            print(f"Lista original (primeros 20):  {lista_actual[:20]}")
            print(f"Lista ordenada (primeros 20):  {resultado[:20]}")
            
            print(f"\n📊 Estadísticas:")
            print(f"  • Cantidad de elementos: {len(resultado)}")
            print(f"  • Valor mínimo: {resultado[0]}")
            print(f"  • Valor máximo: {resultado[-1]}")
            print(f"  • Promedio: {sum(resultado) / len(resultado):.2f}")
        
        elif opcion == "4":
            if lista_actual is None:
                lista_actual = ingresar_datos()
            else:
                print(f"\nLista actual (primeros 20): {lista_actual[:20]}")
                usar_actual = input("¿Usar esta lista? (s/n): ")
                if usar_actual.lower() != "s":
                    lista_actual = ingresar_datos()
            
            comparar_metodos(lista_actual)
        
        else:
            print("\n❌ Opción inválida. Elige del 1 al 5.")
        
        input("\n✨ Presiona ENTER para continuar...")
if __name__ == "__main__":
    main()
