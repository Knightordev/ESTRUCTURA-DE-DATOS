
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
            },
            'carlos.ruiz@email.com': {
                'nombre': 'Carlos Ruiz',
                'id': 'USR-003',
                'plan': 'Premium',
                'fecha_registro': '2023-02-10',
                'ultimo_acceso': '2024-11-29'
            },
            'ana.martinez@email.com': {
                'nombre': 'Ana Martínez',
                'id': 'USR-004',
                'plan': 'Empresarial',
                'fecha_registro': '2023-04-05',
                'ultimo_acceso': '2024-12-01'
            },
            'luis.torres@email.com': {
                'nombre': 'Luis Torres',
                'id': 'USR-005',
                'plan': 'Básico',
                'fecha_registro': '2023-05-18',
                'ultimo_acceso': '2024-11-27'
            },
            'sofia.garcia@email.com': {
                'nombre': 'Sofia García',
                'id': 'USR-006',
                'plan': 'Premium',
                'fecha_registro': '2023-06-30',
                'ultimo_acceso': '2024-11-25'
            },
            'pedro.sanchez@email.com': {
                'nombre': 'Pedro Sánchez',
                'id': 'USR-007',
                'plan': 'Básico',
                'fecha_registro': '2023-07-12',
                'ultimo_acceso': '2024-11-26'
            },
            'laura.diaz@email.com': {
                'nombre': 'Laura Díaz',
                'id': 'USR-008',
                'plan': 'Premium',
                'fecha_registro': '2023-08-25',
                'ultimo_acceso': '2024-12-01'
            },
            'roberto.fernandez@email.com': {
                'nombre': 'Roberto Fernández',
                'id': 'USR-009',
                'plan': 'Empresarial',
                'fecha_registro': '2023-09-14',
                'ultimo_acceso': '2024-11-30'
            },
            'elena.gomez@email.com': {
                'nombre': 'Elena Gómez',
                'id': 'USR-010',
                'plan': 'Premium',
                'fecha_registro': '2023-10-03',
                'ultimo_acceso': '2024-12-01'
            }
        }
        
        self.total_busquedas = 0
        self.busquedas_exitosas = 0
    
    def buscar(self, email):
        print(f"\n{'='*70}")
        print(f"BÚSQUEDA HASH - Email: {email}")
        print(f"{'='*70}")
        
        self.total_busquedas += 1
        inicio = time.time()
        
        # PASO 1: Calcular hash
        print(f"\nPASO 1: Calculando función hash...")
        hash_value = hash(email)
        print(f"   Email: '{email}'")
        print(f"   Hash generado: {hash_value}")
        print(f"   (Este número indica la posición en memoria)")
        
        # PASO 2: Acceso directo
        print(f"\nPASO 2: Accediendo directamente a la posición...")
        print(f"   No se itera, se accede directamente mediante el hash")
        
        # PASO 3: Verificar existencia
        if email in self.usuarios:
            usuario = self.usuarios[email]
            tiempo = time.time() - inicio
            self.busquedas_exitosas += 1
            
            print(f"\n¡USUARIO ENCONTRADO!")
            print(f"\n{'─'*70}")
            print(f"Email:           {email}")
            print(f"Nombre:          {usuario['nombre']}")
            print(f"ID:              {usuario['id']}")
            print(f"Plan:            {usuario['plan']}")
            print(f"Registro:        {usuario['fecha_registro']}")
            print(f"Último acceso:   {usuario['ultimo_acceso']}")
            print(f"{'─'*70}")
            print(f"\n RENDIMIENTO:")
            print(f"   Comparaciones: 1 (acceso directo)")
            print(f"   Tiempo: {tiempo*1000:.4f} ms")
            print(f"   Complejidad: O(1) - tiempo constante")
            
            return usuario
        else:
            tiempo = time.time() - inicio
            
            print(f"\nUSUARIO NO ENCONTRADO")
            print(f"\nRENDIMIENTO:")
            print(f"   Comparaciones: 1")
            print(f"   Tiempo: {tiempo*1000:.4f} ms")
            print(f"   Complejidad: O(1) - tiempo constante")
            
            return None
    
    def agregar_usuario(self, email, nombre, plan):
        """Agrega un nuevo usuario a la tabla hash"""
        if email in self.usuarios:
            print(f"\n Error: El email {email} ya está registrado")
            return False
        
        nuevo_id = f"USR-{len(self.usuarios) + 1:03d}"
        self.usuarios[email] = {
            'nombre': nombre,
            'id': nuevo_id,
            'plan': plan,
            'fecha_registro': '2024-12-01',
            'ultimo_acceso': '2024-12-01'
        }
        
        print(f"\n Usuario agregado exitosamente")
        print(f"   Email: {email}")
        print(f"   ID: {nuevo_id}")
        return True
    
    def eliminar_usuario(self, email):
        """Elimina un usuario de la tabla hash"""
        if email in self.usuarios:
            usuario = self.usuarios[email]
            del self.usuarios[email]
            print(f"\n Usuario eliminado: {usuario['nombre']}")
            return True
        else:
            print(f"\n Usuario no encontrado: {email}")
            return False
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del sistema"""
        print(f"\n{'='*70}")
        print(f"ESTADÍSTICAS DEL SISTEMA")
        print(f"{'='*70}")
        print(f"\nUsuarios registrados:    {len(self.usuarios)}")
        print(f"Total de búsquedas:      {self.total_busquedas}")
        print(f"Búsquedas exitosas:      {self.busquedas_exitosas}")
        print(f"Búsquedas fallidas:      {self.total_busquedas - self.busquedas_exitosas}")
        
        if self.total_busquedas > 0:
            tasa_exito = (self.busquedas_exitosas / self.total_busquedas) * 100
            print(f"Tasa de éxito:           {tasa_exito:.2f}%")
    
    def mostrar_usuarios(self):
        """Muestra todos los usuarios registrados"""
        print(f"\n{'='*70}")
        print(f" TABLA HASH DE USUARIOS REGISTRADOS")
        print(f"{'='*70}")
        print(f"\nTotal de usuarios: {len(self.usuarios)}\n")
        
        for i, (email, usuario) in enumerate(self.usuarios.items(), 1):
            print(f"{i:2d}. {email:30s} │ {usuario['nombre']:20s} │ "
                  f"{usuario['plan']:12s} │ ID: {usuario['id']}")
    
    def buscar_por_plan(self, plan):
        """Busca todos los usuarios con un plan específico"""
        print(f"\n{'='*70}")
        print(f"BUSCANDO USUARIOS CON PLAN: {plan}")
        print(f"{'='*70}\n")
        
        usuarios_encontrados = []
        for email, usuario in self.usuarios.items():
            if usuario['plan'] == plan:
                usuarios_encontrados.append((email, usuario))
        
        if usuarios_encontrados:
            print(f"Encontrados {len(usuarios_encontrados)} usuarios:\n")
            for email, usuario in usuarios_encontrados:
                print(f"   • {usuario['nombre']} ({email}) - ID: {usuario['id']}")
        else:
            print(f"No se encontraron usuarios con el plan '{plan}'")
        
        return usuarios_encontrados


def menu():
    """Menú interactivo del sistema"""
    sistema = BusquedaHash()
    
    while True:
        print(f"\n{'='*70}")
        print(f"{'SISTEMA DE BÚSQUEDA HASH - AUTENTICACIÓN DE USUARIOS':^70}")
        print(f"{'='*70}")
        print("\n1.  Buscar usuario por email")
        print("2.  Ver todos los usuarios")
        print("3.  Agregar nuevo usuario")
        print("4.  Eliminar usuario")
        print("5.  Buscar usuarios por plan")
        print("6.  Ver estadísticas")
        print("7.  Ejecutar búsquedas de ejemplo")
        print("8.  Ver explicación del método Hash")
        print("0.  Salir")
        print(f"\n{'='*70}")
        
        opcion = input("\n Selecciona una opción: ")
        
        if opcion == '1':
            email = input("\n Ingresa el email del usuario: ").lower().strip()
            sistema.buscar(email)
            input("\n⏸  Presiona Enter para continuar...")
            
        elif opcion == '2':
            sistema.mostrar_usuarios()
            input("\n⏸  Presiona Enter para continuar...")
            
        elif opcion == '3':
            print("\n AGREGAR NUEVO USUARIO")
            email = input("Email: ").lower().strip()
            nombre = input("Nombre completo: ").strip()
            print("\nPlanes disponibles: Básico, Premium, Empresarial")
            plan = input("Plan: ").capitalize().strip()
            sistema.agregar_usuario(email, nombre, plan)
            input("\n⏸  Presiona Enter para continuar...")
            
        elif opcion == '4':
            email = input("\n Email del usuario a eliminar: ").lower().strip()
            sistema.eliminar_usuario(email)
            input("\n⏸  Presiona Enter para continuar...")
            
        elif opcion == '5':
            print("\nPlanes disponibles: Básico, Premium, Empresarial")
            plan = input("Plan a buscar: ").capitalize().strip()
            sistema.buscar_por_plan(plan)
            input("\n⏸  Presiona Enter para continuar...")
            
        elif opcion == '6':
            sistema.mostrar_estadisticas()
            input("\n⏸  Presiona Enter para continuar...")
            
        elif opcion == '7':
            print("\n EJECUTANDO BÚSQUEDAS DE EJEMPLO...\n")
            
            print("="*70)
            print("EJEMPLO 1: Usuario que SÍ existe")
            print("="*70)
            sistema.buscar('maria.lopez@email.com')
            input("\n⏸ Presiona Enter para continuar...")
            
            print("\n" + "="*70)
            print("EJEMPLO 2: Usuario que NO existe")
            print("="*70)
            sistema.buscar('usuario.inexistente@email.com')
            input("\n⏸  Presiona Enter para continuar...")
            
            print("\n" + "="*70)
            print("EJEMPLO 3: Búsqueda rápida múltiple")
            print("="*70)
            emails = ['juan.perez@email.com', 'sofia.garcia@email.com', 'pedro.sanchez@email.com']
            for email in emails:
                sistema.buscar(email)
                print("\n" + "-"*70)
            input("\n⏸ Presiona Enter para continuar...")
            
        elif opcion == '8':
            mostrar_explicacion()
            input("\n⏸ Presiona Enter para continuar...")
            
        elif opcion == '0':
            print("\n" + "="*70)
            print("¡Gracias por usar el sistema! 👋")
            print("="*70 + "\n")
            break
            
        else:
            print("\n Opción inválida. Por favor, intenta de nuevo.")


def mostrar_explicacion():
    """Muestra la explicación detallada del método Hash"""
    print(f"\n{'='*70}")
    print(f"{' EXPLICACIÓN DEL MÉTODO HASH':^70}")
    print(f"{'='*70}")
    
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                    ¿EN QUÉ CONSISTE?                             ║
╚══════════════════════════════════════════════════════════════════╝

La búsqueda hash utiliza una FUNCIÓN HASH que convierte una clave
(como un email) en un número que indica la POSICIÓN EXACTA donde
está almacenado el dato en memoria.

PROCESO:
1. Tomas la clave (email): "maria.lopez@email.com"
2. Aplicas función hash: hash("maria.lopez@email.com") → 8472648392
3. Ese número te dice EXACTAMENTE dónde está guardada la información
4. Accedes DIRECTAMENTE sin buscar

Es como tener un ÍNDICE que te dice exactamente en qué página está
cada cosa, sin tener que hojear todo el libro.

╔══════════════════════════════════════════════════════════════════╗
║              ¿POR QUÉ USAR BÚSQUEDA HASH?                        ║
╚══════════════════════════════════════════════════════════════════╝

✅ VENTAJAS:
• Búsqueda en O(1) - TIEMPO CONSTANTE
• No importa si hay 10 o 10,000,000 de usuarios
• Siempre toma 1 operación
• Ideal para claves únicas (emails, IDs, usernames)
• Usado en: Bases de datos, caché, autenticación

📊 COMPARACIÓN:
   Usuarios    │  Secuencial  │   Binaria   │    Hash
   ───────────────────────────────────────────────────
        10     │      5       │      4      │     1
       100     │     50       │      7      │     1
     1,000     │    500       │     10      │     1
   1,000,000   │  500,000     │     20      │     1

╔══════════════════════════════════════════════════════════════════╗
║           ¿SE PUEDE MEJORAR CON OTRO MÉTODO?                     ║
╚══════════════════════════════════════════════════════════════════╝

❌ NO - La búsqueda hash es el método MÁS RÁPIDO posible para
búsquedas por clave única.

⚠️  CONSIDERACIONES:
• Requiere más memoria que otros métodos
• No mantiene orden (no puedes listar "en orden alfabético")
• Puede haber colisiones (dos claves con mismo hash)
• Python maneja colisiones automáticamente

🔄 ALTERNATIVAS (para casos específicos):
• Si necesitas ORDEN: Árbol binario balanceado (O(log n))
• Si necesitas RANGO: Búsqueda binaria (O(log n))
• Si tienes POCOS datos: Búsqueda secuencial (O(n))

╔══════════════════════════════════════════════════════════════════╗
║                      CONCLUSIONES                                ║
╚══════════════════════════════════════════════════════════════════╝

📌 COMPLEJIDAD TEMPORAL: O(1) - tiempo constante
📌 COMPLEJIDAD ESPACIAL: O(n) - necesita espacio para la tabla

✨ USOS REALES:
• Sistemas de autenticación (login)
• Bases de datos (índices)
• Caché de aplicaciones
• Diccionarios y mapas
• Almacenamiento de sesiones
• DNS (resolución de dominios)

💡 CUÁNDO USARLA:
• Tienes una clave ÚNICA (email, ID, username)
• Necesitas velocidad máxima
• No te importa el orden de los datos
• Haces MUCHAS búsquedas

❌ CUÁNDO NO USARLA:
• Necesitas mantener orden
• Necesitas búsquedas por rango
• Tienes muy pocos datos (< 10)
• La memoria es muy limitada

╔══════════════════════════════════════════════════════════════════╗
║                    ANALOGÍA DEL MUNDO REAL                       ║
╚══════════════════════════════════════════════════════════════════╝

🏢 EDIFICIO DE APARTAMENTOS:
• Cada apartamento tiene un número ÚNICO (email)
• No buscas tocando todas las puertas
• Vas DIRECTO al apartamento #305
• Así funciona la tabla hash: acceso directo

vs.

📚 BIBLIOTECA SIN SISTEMA:
• Búsqueda secuencial = revisar libro por libro
• Búsqueda binaria = ir por secciones dividiendo
• Hash = saber EXACTAMENTE en qué estante está
    """)


def main():
    """Función principal"""
    print(f"\n{'='*70}")
    print(f"{'BIENVENIDO AL SISTEMA DE BÚSQUEDA HASH':^70}")
    print(f"{'='*70}")
    print("\nEste programa demuestra el funcionamiento de la búsqueda hash")
    print("en un sistema de autenticación de usuarios.\n")
    input("Presiona Enter para comenzar...")
    
    menu()


if __name__ == "__main__":
    main()


"""
╔══════════════════════════════════════════════════════════════════╗
║                  DOCUMENTACIÓN DEL CÓDIGO                        ║
╚══════════════════════════════════════════════════════════════════╝

ESTRUCTURA:
• BusquedaHash: Clase principal con la tabla hash
• buscar(): Método de búsqueda O(1)
• agregar_usuario(): Agregar nuevos usuarios
• eliminar_usuario(): Eliminar usuarios existentes
• buscar_por_plan(): Búsqueda por criterio adicional
• menu(): Interfaz interactiva

COMPLEJIDAD:
• Búsqueda:    O(1) - tiempo constante
• Inserción:   O(1) - tiempo constante
• Eliminación: O(1) - tiempo constante
• Espacio:     O(n) - proporcional al número de usuarios

PARA EJECUTAR:
$ python busqueda_hash.py

PARA GITHUB:
$ git add busqueda_hash.py
$ git commit -m "Implementación de búsqueda hash"
$ git push origin main
"""