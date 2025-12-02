import time
class BusquedaHash:
    def __init__(self):
        self.usuarios = {
            'juan.perez@email.com': {
                'nombre': 'Juan Pérez',
                'id': 'USR-001',
                'plan': 'Premium',
                'fecha_registro': '2023-01-15',
                'ultimo_acceso': '2024-11-28'
            },
            'maria.lopez@email.com': {
                'nombre': 'María López',
                'id': 'USR-002',
                'plan': 'Básico',
                'fecha_registro': '2023-03-22',
                'ultimo_acceso': '2024-11-30'
            }
        }
        
        self.total_busquedas = 0
        self.busquedas_exitosas = 0
    
    def buscar(self, email):
        print("\n=== BUSCANDO EN TABLA HASH ===")
        self.total_busquedas += 1
        inicio = time.time()
        
        if email in self.usuarios:
            usuario = self.usuarios[email]
            self.busquedas_exitosas += 1
            tiempo = (time.time() - inicio) * 1000
            
            print("\nUsuario encontrado:")
            for k, v in usuario.items():
                print(f"  {k}: {v}")
            print(f"\nComparaciones: 1 (acceso directo)")
            print(f"Tiempo: {tiempo:.4f} ms")
            return usuario
        
        print("\nUsuario no encontrado")
        return None
    
    def menu_hash(self):
        while True:
            print("\n=== SISTEMA HASH ===")
            print("1. Buscar usuario por email")
            print("2. Mostrar usuarios")
            print("3. Volver al menú principal")
            opcion = input("\nElige opción: ")
            
            if opcion == '1':
                email = input("Email: ").lower().strip()
                self.buscar(email)
            elif opcion == '2':
                print("\nUsuarios registrados:")
                for email, user in self.usuarios.items():
                    print(f" - {email}: {user['nombre']}")
            elif opcion == '3':
                break
            else:
                print("Opción inválida.")


def busqueda_secuencial(lista, elemento_buscado):
    comparaciones = 0
    
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i]['codigo'] == elemento_buscado:
            print(f"\nElemento encontrado en posición {i}")
            print(f"Comparaciones: {comparaciones}")
            return i
    
    print("\nElemento no encontrado")
    print(f"Comparaciones: {comparaciones}")
    return -1


def menu_secuencial():
    inventario = [
        {'codigo': 'P-458', 'nombre': 'Laptop Dell', 'precio': 15000},
        {'codigo': 'P-102', 'nombre': 'Mouse Logitech', 'precio': 350},
        {'codigo': 'P-789', 'nombre': 'Teclado Mecánico', 'precio': 1200},
        {'codigo': 'P-234', 'nombre': 'Monitor Samsung', 'precio': 5000},
        {'codigo': 'P-567', 'nombre': 'Webcam HD', 'precio': 800}
    ]
    
    while True:
        print("\n=== BÚSQUEDA SECUENCIAL ===")
        print("Inventario actual:")
        for p in inventario:
            print(f" - {p['codigo']} | {p['nombre']} | ${p['precio']}")
        
        print("\n1. Buscar producto")
        print("2. Volver al menú principal")
        opcion = input("\nElige opción: ")
        
        if opcion == '1':
            codigo = input("Código del producto: ").strip()
            busqueda_secuencial(inventario, codigo)
        elif opcion == '2':
            break
        else:
            print("Opción inválida.")

def busqueda_binaria(lista, isbn_buscado):
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0
    
    while izquierda <= derecha:
        comparaciones += 1
        medio = (izquierda + derecha) // 2
        isbn_medio = lista[medio]['isbn']
        
        if isbn_medio == isbn_buscado:
            print(f"\nLibro encontrado en posición {medio}")
            print(f"Comparaciones: {comparaciones}")
            return medio
        
        elif isbn_medio < isbn_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    print("\nLibro no encontrado")
    print(f"Comparaciones: {comparaciones}")
    return -1


def menu_binaria():
    biblioteca = [
        {'isbn': 1001, 'titulo': 'Python Fácil'},
        {'isbn': 1050, 'titulo': 'Algoritmos'},
        {'isbn': 1080, 'titulo': 'Ciberseguridad'},
        {'isbn': 1200, 'titulo': 'Machine Learning'},
        {'isbn': 1350, 'titulo': 'Cloud Computing'}
    ]
    
    while True:
        print("\n=== BÚSQUEDA BINARIA ===")
        print("Catálogo (ordenado por ISBN):")
        for l in biblioteca:
            print(f" - {l['isbn']} | {l['titulo']}")
        
        print("\n1. Buscar libro por ISBN")
        print("2. Volver al menú principal")
        opcion = input("\nElige opción: ")
        
        if opcion == '1':
            isbn = int(input("ISBN: "))
            busqueda_binaria(biblioteca, isbn)
        elif opcion == '2':
            break
        else:
            print("Opción inválida.")

def main():
    sistema_hash = BusquedaHash()
    
    while True:
        print("\n" + "="*60)
        print(" SISTEMA GENERAL DE BÚSQUEDAS ".center(60))
        print("="*60)
        print("\n1. Búsqueda Secuencial")
        print("2. Búsqueda Binaria")
        print("3. Búsqueda Hash")
        print("0. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == '1':
            menu_secuencial()
        elif opcion == '2':
            menu_binaria()
        elif opcion == '3':
            sistema_hash.menu_hash()
        elif opcion == '0':
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()
