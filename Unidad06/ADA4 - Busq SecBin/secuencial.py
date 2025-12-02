def busqueda_secuencial(lista, elemento_buscado):
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
