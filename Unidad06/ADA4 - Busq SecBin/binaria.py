"""
EJERCICIO 2: BÚSQUEDA BINARIA
Sistema de Biblioteca con Libros Ordenados por ISBN

Descripción:
Biblioteca digital con catálogo ordenado por ISBN que permite búsquedas
rápidas de libros. Los ISBNs están ordenados numéricamente.
"""

def busqueda_binaria(lista, isbn_buscado):
    izquierda = 0
    derecha = len(lista) - 1
    comparaciones = 0
    
    print(f"\nBuscando ISBN: {isbn_buscado}")
    print(f"Rango inicial: [{izquierda}, {derecha}]")
    
    while izquierda <= derecha:
        comparaciones += 1
        medio = (izquierda + derecha) // 2
        isbn_medio = lista[medio]['isbn']
        
        print(f"\nComparación {comparaciones}:")
        print(f"  Posición media: {medio}")
        print(f"  ISBN medio: {isbn_medio}")
        
        if isbn_medio == isbn_buscado:
            print(f"  ¡Encontrado!")
            print(f"\nTotal de comparaciones: {comparaciones}")
            return medio
        elif isbn_medio < isbn_buscado:
            print(f"  {isbn_buscado} > {isbn_medio}, buscar en mitad derecha")
            izquierda = medio + 1
        else:
            print(f"  {isbn_buscado} < {isbn_medio}, buscar en mitad izquierda")
            derecha = medio - 1
    
    print(f"\nLibro no encontrado")
    print(f"Total de comparaciones: {comparaciones}")
    return -1


def busqueda_binaria_recursiva(lista, isbn_buscado, izq, der, comparaciones=0):
    if izq > der:
        return -1, comparaciones
    
    medio = (izq + der) // 2
    comparaciones += 1
    isbn_medio = lista[medio]['isbn']
    
    if isbn_medio == isbn_buscado:
        return medio, comparaciones
    elif isbn_medio < isbn_buscado:
        return busqueda_binaria_recursiva(lista, isbn_buscado, medio + 1, der, comparaciones)
    else:
        return busqueda_binaria_recursiva(lista, isbn_buscado, izq, medio - 1, comparaciones)


def main():
    biblioteca = [
        {'isbn': 1001, 'titulo': 'Python para Principiantes', 'autor': 'García López'},
        {'isbn': 1015, 'titulo': 'Algoritmos y Estructuras', 'autor': 'Martínez Ruiz'},
        {'isbn': 1023, 'titulo': 'Bases de Datos Avanzadas', 'autor': 'Sánchez Torres'},
        {'isbn': 1047, 'titulo': 'Inteligencia Artificial', 'autor': 'Rodríguez Vega'},
        {'isbn': 1089, 'titulo': 'Desarrollo Web Moderno', 'autor': 'Hernández Cruz'},
        {'isbn': 1102, 'titulo': 'Ciberseguridad Práctica', 'autor': 'Pérez Morales'},
        {'isbn': 1156, 'titulo': 'Machine Learning Básico', 'autor': 'González Ramos'},
        {'isbn': 1203, 'titulo': 'Cloud Computing', 'autor': 'Díaz Fernández'},
        {'isbn': 1267, 'titulo': 'DevOps y CI/CD', 'autor': 'López Herrera'},
        {'isbn': 1334, 'titulo': 'Programación Funcional', 'autor': 'Torres Jiménez'}
    ]
    
    print("="*70)
    print("SISTEMA DE BÚSQUEDA DE LIBROS EN BIBLIOTECA DIGITAL")
    print("="*70)
    print("\nCatálogo ordenado por ISBN:")
    for i, libro in enumerate(biblioteca):
        print(f"{i}. ISBN {libro['isbn']} - {libro['titulo']} - {libro['autor']}")
    
    print("\n" + "="*70)
    print("BÚSQUEDA 1: Libro en posición media (ISBN 1102)")
    print("="*70)
    resultado = busqueda_binaria(biblioteca, 1102)
    if resultado != -1:
        print(f"\nLibro encontrado:")
        print(f"  Título: {biblioteca[resultado]['titulo']}")
        print(f"  Autor: {biblioteca[resultado]['autor']}")
    

    print("\n" + "="*70)
    print("BÚSQUEDA 2: Libro no existente (ISBN 1500)")
    print("="*70)
    resultado = busqueda_binaria(biblioteca, 1500)
    

    print("\n" + "="*70)
    print("BÚSQUEDA 3: Primer libro (ISBN 1001)")
    print("="*70)
    resultado = busqueda_binaria(biblioteca, 1001)
    if resultado != -1:
        print(f"\nLibro encontrado:")
        print(f"  Título: {biblioteca[resultado]['titulo']}")
    
    print("\n" + "="*70)
    print("BÚSQUEDA 4: Versión recursiva (ISBN 1267)")
    print("="*70)
    resultado, comps = busqueda_binaria_recursiva(biblioteca, 1267, 0, len(biblioteca)-1)
    if resultado != -1:
        print(f"Libro encontrado en posición {resultado}")
        print(f"Comparaciones: {comps}")
        print(f"Título: {biblioteca[resultado]['titulo']}")


if __name__ == "__main__":
    main()


"""
EXPLICACIÓN DEL EJERCICIO:

1. ¿En qué consiste?
   - Sistema de biblioteca con catálogo ordenado por ISBN
   - Búsqueda dividiendo el espacio de búsqueda a la mitad en cada paso
   - Compara con el elemento medio y descarta la mitad incorrecta

2. ¿Por qué usar búsqueda binaria?
   - El catálogo ESTÁ ORDENADO por ISBN (requisito fundamental)
   - Extremadamente eficiente: reduce búsquedas exponencialmente
   - En 10 elementos máximo 4 comparaciones vs 10 en secuencial
   - En 1,000,000 elementos máximo 20 comparaciones vs 1,000,000
   - Ideal para catálogos grandes con consultas frecuentes

3. ¿Se puede mejorar con otro método?
   - Para UNA búsqueda: NO, es óptima para listas ordenadas
   - Para MUCHAS búsquedas: SÍ, usar hash table (diccionario):
     * biblioteca_dict = {libro['isbn']: libro for libro in biblioteca}
     * O(1) constante en vez de O(log n)
   - Árbol binario de búsqueda balanceado:
     * Mantiene orden Y permite O(log n) en búsqueda/inserción/eliminación
   - Interpolación si ISBNs tienen distribución uniforme

4. CONCLUSIONES:
   - Complejidad temporal: O(log n) - divide lista a la mitad cada vez
   - Complejidad espacial: O(1) iterativa, O(log n) recursiva (pila)
   - REQUISITO CRÍTICO: Lista debe estar ordenada
   - Ventajas: Muy rápida en listas grandes, eficiente en memoria
   - Desventajas: Requiere ordenamiento previo O(n log n)
   - Comparación: 1M elementos = 20 comparaciones vs 500,000 promedio secuencial
   - Uso real: Bases de datos, diccionarios, índices, sistemas de archivos
   
   EJEMPLO PRÁCTICO:
   - Lista de 1,024 elementos:
     * Búsqueda secuencial: hasta 1,024 comparaciones (promedio 512)
     * Búsqueda binaria: máximo 10 comparaciones
   - ¡Más de 100x más rápida!
"""