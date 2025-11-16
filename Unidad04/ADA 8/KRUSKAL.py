import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class UnionFind:
    """Estructura de datos Union-Find para detectar ciclos"""
    def __init__(self, nodos):
        self.padre = {nodo: nodo for nodo in nodos}
        self.rango = {nodo: 0 for nodo in nodos}
    
    def encontrar(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.encontrar(self.padre[nodo])
        return self.padre[nodo]
    
    def unir(self, nodo1, nodo2):
        raiz1 = self.encontrar(nodo1)
        raiz2 = self.encontrar(nodo2)
        
        if raiz1 == raiz2:
            return False
        
        if self.rango[raiz1] < self.rango[raiz2]:
            self.padre[raiz1] = raiz2
        elif self.rango[raiz1] > self.rango[raiz2]:
            self.padre[raiz2] = raiz1
        else:
            self.padre[raiz2] = raiz1
            self.rango[raiz1] += 1
        
        return True

class KruskalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de Kruskal - Visualizador")
        self.root.geometry("950x750")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.aristas = []
        
        # Configurar interfaz
        self.setup_ui()
        self.cargar_grafo_ejemplo()
        
    def setup_ui(self):
        # Título
        titulo = tk.Label(self.root, text="Algoritmo de Kruskal", 
                         font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=10)
        
        # Subtítulo
        subtitulo = tk.Label(self.root, text="Árbol de Expansión Mínima (MST)", 
                            font=('Arial', 11, 'italic'), bg='#f0f0f0', fg='#7f8c8d')
        subtitulo.pack(pady=2)
        
        # Frame para entrada de datos
        frame_entrada = tk.LabelFrame(self.root, text="Configuración del Grafo", 
                                     font=('Arial', 12, 'bold'), bg='#f0f0f0', padx=10, pady=10)
        frame_entrada.pack(padx=20, pady=10, fill='x')
        
        # Entrada de aristas
        tk.Label(frame_entrada, text="Agregar Arista (Formato: A B 5):", 
                bg='#f0f0f0', font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=5)
        
        self.entry_arista = tk.Entry(frame_entrada, width=30, font=('Arial', 10))
        self.entry_arista.grid(row=0, column=1, padx=5, pady=5)
        
        btn_agregar = tk.Button(frame_entrada, text="Agregar Arista", 
                               command=self.agregar_arista, bg='#3498db', fg='white',
                               font=('Arial', 10, 'bold'), cursor='hand2')
        btn_agregar.grid(row=0, column=2, padx=5, pady=5)
        
        # Nota
        nota = tk.Label(frame_entrada, text="Nota: Las aristas son no dirigidas (A-B es lo mismo que B-A)", 
                       bg='#f0f0f0', font=('Arial', 9, 'italic'), fg='#7f8c8d')
        nota.grid(row=1, column=0, columnspan=3, pady=5)
        
        # Botones de acción
        frame_botones = tk.Frame(frame_entrada, bg='#f0f0f0')
        frame_botones.grid(row=2, column=0, columnspan=3, pady=10)
        
        btn_ejecutar = tk.Button(frame_botones, text="Ejecutar Kruskal", 
                                command=self.ejecutar_kruskal, bg='#27ae60', fg='white',
                                font=('Arial', 11, 'bold'), cursor='hand2', width=18)
        btn_ejecutar.pack(side='left', padx=5)
        
        btn_limpiar = tk.Button(frame_botones, text="Limpiar Grafo", 
                               command=self.limpiar_grafo, bg='#e74c3c', fg='white',
                               font=('Arial', 11, 'bold'), cursor='hand2', width=15)
        btn_limpiar.pack(side='left', padx=5)
        
        btn_ejemplo = tk.Button(frame_botones, text="Cargar Ejemplo", 
                               command=self.cargar_grafo_ejemplo, bg='#f39c12', fg='white',
                               font=('Arial', 11, 'bold'), cursor='hand2', width=15)
        btn_ejemplo.pack(side='left', padx=5)
        
        # Frame para resultados
        frame_resultados = tk.LabelFrame(self.root, text="Resultados", 
                                        font=('Arial', 12, 'bold'), bg='#f0f0f0', padx=10, pady=10)
        frame_resultados.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Área de texto para resultados
        self.texto_resultado = scrolledtext.ScrolledText(frame_resultados, 
                                                         width=90, height=22, 
                                                         font=('Courier', 9), 
                                                         bg='#2c3e50', fg='#ecf0f1',
                                                         insertbackground='white')
        self.texto_resultado.pack(fill='both', expand=True)
        
    def agregar_arista(self):
        try:
            entrada = self.entry_arista.get().strip().split()
            if len(entrada) != 3:
                raise ValueError("Formato incorrecto")
            
            nodo1, nodo2, peso = entrada[0], entrada[1], float(entrada[2])
            
            if peso < 0:
                messagebox.showerror("Error", "El peso debe ser no negativo")
                return
            
            # Agregar arista (no dirigida)
            self.aristas.append((nodo1, nodo2, peso))
            
            self.entry_arista.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Arista agregada: {nodo1} -- {nodo2} (peso: {peso})")
            self.mostrar_grafo_actual()
            
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Use: Nodo1 Nodo2 Peso\nEjemplo: A B 5")
    
    def cargar_grafo_ejemplo(self):
        self.aristas = [
            ('A', 'B', 4),
            ('A', 'C', 3),
            ('A', 'D', 5),
            ('B', 'C', 2),
            ('B', 'D', 6),
            ('C', 'D', 7),
            ('C', 'E', 4),
            ('D', 'E', 5),
            ('D', 'F', 8),
            ('E', 'F', 6)
        ]
        self.mostrar_grafo_actual()
        messagebox.showinfo("Éxito", "Grafo de ejemplo cargado correctamente")
    
    def limpiar_grafo(self):
        self.aristas = []
        self.texto_resultado.delete(1.0, tk.END)
        messagebox.showinfo("Éxito", "Grafo limpiado")
    
    def mostrar_grafo_actual(self):
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "GRAFO ACTUAL (No Dirigido)\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n\n")
        
        if not self.aristas:
            self.texto_resultado.insert(tk.END, "No hay aristas en el grafo.\n")
            return
        
        self.texto_resultado.insert(tk.END, "Aristas:\n")
        for nodo1, nodo2, peso in sorted(self.aristas, key=lambda x: x[2]):
            self.texto_resultado.insert(tk.END, f"  {nodo1} -- {nodo2}: {peso}\n")
        
        # Calcular y mostrar nodos
        nodos = set()
        for nodo1, nodo2, _ in self.aristas:
            nodos.add(nodo1)
            nodos.add(nodo2)
        
        self.texto_resultado.insert(tk.END, f"\nTotal de nodos: {len(nodos)}\n")
        self.texto_resultado.insert(tk.END, f"Nodos: {', '.join(sorted(nodos))}\n")
        self.texto_resultado.insert(tk.END, f"Total de aristas: {len(self.aristas)}\n")
        
        peso_total = sum(peso for _, _, peso in self.aristas)
        self.texto_resultado.insert(tk.END, f"Peso total del grafo: {peso_total}\n")
    
    def kruskal(self):
        if not self.aristas:
            return None, None, None
        
        # Obtener todos los nodos únicos
        nodos = set()
        for nodo1, nodo2, _ in self.aristas:
            nodos.add(nodo1)
            nodos.add(nodo2)
        
        # Ordenar aristas por peso
        aristas_ordenadas = sorted(self.aristas, key=lambda x: x[2])
        
        # Inicializar Union-Find
        uf = UnionFind(nodos)
        
        # Lista para almacenar las aristas del MST y el proceso
        mst = []
        proceso = []
        peso_total = 0
        aristas_rechazadas = []
        
        # Procesar cada arista
        for nodo1, nodo2, peso in aristas_ordenadas:
            if uf.unir(nodo1, nodo2):
                mst.append((nodo1, nodo2, peso))
                peso_total += peso
                proceso.append((nodo1, nodo2, peso, True, peso_total))
            else:
                aristas_rechazadas.append((nodo1, nodo2, peso))
                proceso.append((nodo1, nodo2, peso, False, peso_total))
            
            # Si ya tenemos n-1 aristas, el MST está completo
            if len(mst) == len(nodos) - 1:
                break
        
        return mst, peso_total, proceso, aristas_ordenadas, aristas_rechazadas, nodos
    
    def ejecutar_kruskal(self):
        if not self.aristas:
            messagebox.showerror("Error", "El grafo está vacío. Agregue aristas primero.")
            return
        
        resultado = self.kruskal()
        if resultado[0] is None:
            messagebox.showerror("Error", "Error al ejecutar el algoritmo")
            return
        
        mst, peso_total, proceso, aristas_ordenadas, aristas_rechazadas, nodos = resultado
        
        # Mostrar resultados
        self.texto_resultado.delete(1.0, tk.END)
        
        # Encabezado
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "ALGORITMO DE KRUSKAL - ÁRBOL DE EXPANSIÓN MÍNIMA\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n\n")
        
        self.texto_resultado.insert(tk.END, f"Total de nodos: {len(nodos)}\n")
        self.texto_resultado.insert(tk.END, f"Nodos: {', '.join(sorted(nodos))}\n")
        self.texto_resultado.insert(tk.END, f"Total de aristas: {len(self.aristas)}\n")
        self.texto_resultado.insert(tk.END, f"Aristas necesarias para MST: {len(nodos) - 1}\n")
        
        # Aristas ordenadas
        self.texto_resultado.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "ARISTAS ORDENADAS POR PESO:\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        for i, (nodo1, nodo2, peso) in enumerate(aristas_ordenadas, 1):
            self.texto_resultado.insert(tk.END, f"{i}. {nodo1} -- {nodo2}: {peso}\n")
        
        # Proceso de ejecución
        self.texto_resultado.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "PROCESO DE CONSTRUCCIÓN DEL MST:\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n\n")
        
        for i, (nodo1, nodo2, peso, aceptada, peso_acum) in enumerate(proceso, 1):
            if aceptada:
                self.texto_resultado.insert(tk.END, 
                    f"{i}. ✓ ACEPTADA: {nodo1} -- {nodo2} (peso: {peso})\n")
                self.texto_resultado.insert(tk.END, 
                    f"   Peso acumulado: {peso_acum}\n")
            else:
                self.texto_resultado.insert(tk.END, 
                    f"{i}. ✗ RECHAZADA: {nodo1} -- {nodo2} (peso: {peso}) - Formaría ciclo\n")
        
        # MST resultante
        self.texto_resultado.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "ÁRBOL DE EXPANSIÓN MÍNIMA (MST):\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n\n")
        
        self.texto_resultado.insert(tk.END, f"Peso total del MST: {peso_total}\n\n")
        self.texto_resultado.insert(tk.END, "Aristas en el MST:\n")
        for i, (nodo1, nodo2, peso) in enumerate(mst, 1):
            self.texto_resultado.insert(tk.END, f"  {i}. {nodo1} -- {nodo2} (peso: {peso})\n")
        
        # Grados en el MST
        grados = {}
        for nodo1, nodo2, _ in mst:
            grados[nodo1] = grados.get(nodo1, 0) + 1
            grados[nodo2] = grados.get(nodo2, 0) + 1
        
        self.texto_resultado.insert(tk.END, "\nGrado de cada nodo en el MST:\n")
        for nodo in sorted(grados.keys()):
            grado = grados[nodo]
            tipo = "Hoja" if grado == 1 else f"Interno"
            self.texto_resultado.insert(tk.END, f"  {nodo}: {grado} ({tipo})\n")
        
        # Estadísticas
        self.texto_resultado.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "ESTADÍSTICAS:\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        
        peso_grafo_completo = sum(peso for _, _, peso in self.aristas)
        self.texto_resultado.insert(tk.END, f"Peso total de todas las aristas: {peso_grafo_completo}\n")
        self.texto_resultado.insert(tk.END, f"Peso del MST: {peso_total}\n")
        self.texto_resultado.insert(tk.END, 
            f"Ahorro: {peso_grafo_completo - peso_total} "
            f"({((peso_grafo_completo - peso_total) / peso_grafo_completo * 100):.1f}%)\n")
        self.texto_resultado.insert(tk.END, f"Aristas originales: {len(self.aristas)}\n")
        self.texto_resultado.insert(tk.END, f"Aristas en MST: {len(mst)}\n")
        self.texto_resultado.insert(tk.END, f"Aristas rechazadas: {len(aristas_rechazadas)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = KruskalApp(root)
    root.mainloop()