"""
EJERCICIO 1: BÚSQUEDA SECUENCIAL
Sistema de Inventario de Productos

Descripción:
Sistema que busca productos en un inventario desordenado donde los productos
llegan en orden aleatorio según las compras realizadas.
"""

def busqueda_secuencial(lista, elemento_buscado):
    """
    Busca un elemento en una lista de forma secuencial.
    
    Args:
        lista: Lista donde buscar
        elemento_buscado: Elemento a encontrar
    
    Returns:
        Índice del elemento si se encuentra, -1 si no existe
    """
    comparaciones = 0
    
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i]['codigo'] == elemento_buscado:
            print(f"Elemento encontrado en la posición {i}")
            print(f"Comparaciones realizadas: {comparaciones}")
            return i
    
    print(f"Elemento no encontrado")
    print(f"Comparaciones realizadas: {comparaciones}")
    return -1


def main():
    inventario = [
        {'codigo': 'P-458', 'nombre': 'Laptop Dell', 'precio': 15000},
        {'codigo': 'P-102', 'nombre': 'Mouse Logitech', 'precio': 350},
        {'codigo': 'P-789', 'nombre': 'Teclado Mecánico', 'precio': 1200},
        {'codigo': 'P-234', 'nombre': 'Monitor Samsung', 'precio': 5000},
        {'codigo': 'P-567', 'nombre': 'Webcam HD', 'precio': 800},
        {'codigo': 'P-901', 'nombre': 'Audífonos Sony', 'precio': 2500},
        {'codigo': 'P-345', 'nombre': 'Disco Duro 1TB', 'precio': 1800},
        {'codigo': 'P-678', 'nombre': 'Memoria RAM 16GB', 'precio': 2200}
    ]
    
    print("="*60)
    print("SISTEMA DE BÚSQUEDA DE PRODUCTOS EN INVENTARIO")
    print("="*60)
    print("\nInventario actual:")
    for i, producto in enumerate(inventario):
        print(f"{i}. {producto['codigo']} - {producto['nombre']} - ${producto['precio']}")
    

    print("\n" + "="*60)
    print("BÚSQUEDA 1: Producto existente (P-567)")
    print("="*60)
    resultado = busqueda_secuencial(inventario, 'P-567')
    if resultado != -1:
        print(f"Producto: {inventario[resultado]['nombre']}")
        print(f"Precio: ${inventario[resultado]['precio']}")
    
    print("\n" + "="*60)
    print("BÚSQUEDA 2: Producto no existente (P-999)")
    print("="*60)
    resultado = busqueda_secuencial(inventario, 'P-999')
    
    print("\n" + "="*60)
    print("BÚSQUEDA 3: Primer elemento (P-458)")
    print("="*60)
    resultado = busqueda_secuencial(inventario, 'P-458')
    if resultado != -1:
        print(f"Producto: {inventario[resultado]['nombre']}")


if __name__ == "__main__":
    main()


"""
EXPLICACIÓN DEL EJERCICIO:

1. ¿En qué consiste?
   - Sistema de inventario donde los productos se almacenan en orden de llegada
   - Busca productos por código sin importar el orden
   - Recorre elemento por elemento hasta encontrar el código buscado

2. ¿Por qué usar búsqueda secuencial?
   - El inventario NO está ordenado (productos llegan aleatoriamente)
   - Es imposible usar búsqueda binaria en datos desordenados
   - Cada búsqueda debe revisar elemento por elemento
   - Ideal cuando el orden no importa o no se puede mantener

3. ¿Se puede mejorar con otro método?
   - SÍ, con un diccionario (hash table):
     * inventario_dict = {prod['codigo']: prod for prod in inventario}
     * Búsqueda en O(1) en vez de O(n)
   - O con búsqueda binaria SI ordenamos primero:
     * Costo: O(n log n) para ordenar + O(log n) por búsqueda
     * Solo vale la pena si haremos MUCHAS búsquedas

4. CONCLUSIONES:
   - Complejidad temporal: O(n) - revisa hasta n elementos
   - Complejidad espacial: O(1) - no usa memoria extra
   - Ventajas: Simple, funciona en cualquier lista, no requiere ordenamiento
   - Desventajas: Lento para listas grandes (peor caso: n comparaciones)
   - Uso real: Listas pequeñas, datos desordenados, búsquedas poco frecuentes
"""