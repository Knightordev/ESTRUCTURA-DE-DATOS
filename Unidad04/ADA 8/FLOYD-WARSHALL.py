import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class FloydWarshallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de Floyd-Warshall - Visualizador")
        self.root.geometry("950x750")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.grafo = {}
        
        # Configurar interfaz
        self.setup_ui()
        self.cargar_grafo_ejemplo()
        
    def setup_ui(self):
        # Título
        titulo = tk.Label(self.root, text="Algoritmo de Floyd-Warshall", 
                         font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=10)
        
        # Frame para entrada de datos
        frame_entrada = tk.LabelFrame(self.root, text="Configuración del Grafo", 
                                     font=('Arial', 12, 'bold'), bg='#f0f0f0', padx=10, pady=10)
        frame_entrada.pack(padx=20, pady=10, fill='x')
        
        # Entrada de aristas
        tk.Label(frame_entrada, text="Agregar Arista Dirigida (Formato: A B 5):", 
                bg='#f0f0f0', font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=5)
        
        self.entry_arista = tk.Entry(frame_entrada, width=30, font=('Arial', 10))
        self.entry_arista.grid(row=0, column=1, padx=5, pady=5)
        
        btn_agregar = tk.Button(frame_entrada, text="Agregar Arista", 
                               command=self.agregar_arista, bg='#3498db', fg='white',
                               font=('Arial', 10, 'bold'), cursor='hand2')
        btn_agregar.grid(row=0, column=2, padx=5, pady=5)
        
        # Nota sobre aristas dirigidas
        nota = tk.Label(frame_entrada, text="Nota: Las aristas son dirigidas (A -> B)", 
                       bg='#f0f0f0', font=('Arial', 9, 'italic'), fg='#7f8c8d')
        nota.grid(row=1, column=0, columnspan=3, pady=5)
        
        # Botones de acción
        frame_botones = tk.Frame(frame_entrada, bg='#f0f0f0')
        frame_botones.grid(row=2, column=0, columnspan=3, pady=10)
        
        btn_ejecutar = tk.Button(frame_botones, text="Ejecutar Floyd-Warshall", 
                                command=self.ejecutar_floyd, bg='#27ae60', fg='white',
                                font=('Arial', 11, 'bold'), cursor='hand2', width=20)
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
            
            # Agregar arista dirigida
            if nodo1 not in self.grafo:
                self.grafo[nodo1] = {}
            
            self.grafo[nodo1][nodo2] = peso
            
            # Asegurar que nodo2 existe en el grafo
            if nodo2 not in self.grafo:
                self.grafo[nodo2] = {}
            
            self.entry_arista.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Arista agregada: {nodo1} -> {nodo2} (peso: {peso})")
            self.mostrar_grafo_actual()
            
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Use: Nodo1 Nodo2 Peso\nEjemplo: A B 5")
    
    def cargar_grafo_ejemplo(self):
        self.grafo = {
            'A': {'B': 3, 'C': 8, 'E': -4},
            'B': {'D': 1, 'E': 7},
            'C': {'B': 4},
            'D': {'A': 2, 'C': -5},
            'E': {'D': 6}
        }
        self.mostrar_grafo_actual()
        messagebox.showinfo("Éxito", "Grafo de ejemplo cargado correctamente")
    
    def limpiar_grafo(self):
        self.grafo = {}
        self.texto_resultado.delete(1.0, tk.END)
        messagebox.showinfo("Éxito", "Grafo limpiado")
    
    def mostrar_grafo_actual(self):
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "GRAFO ACTUAL (Dirigido)\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n\n")
        
        for nodo in sorted(self.grafo.keys()):
            if self.grafo[nodo]:
                vecinos = ', '.join([f"{v}({p})" for v, p in self.grafo[nodo].items()])
                self.texto_resultado.insert(tk.END, f"{nodo} -> {vecinos}\n")
            else:
                self.texto_resultado.insert(tk.END, f"{nodo} -> (sin aristas salientes)\n")
    
    def floyd_warshall(self):
        nodos = list(self.grafo.keys())
        n = len(nodos)
        indice = {nodo: i for i, nodo in enumerate(nodos)}
        
        # Inicializar matrices
        INF = float('inf')
        distancias = [[INF] * n for _ in range(n)]
        siguiente = [[None] * n for _ in range(n)]
        
        # Distancia de un nodo a sí mismo es 0
        for i in range(n):
            distancias[i][i] = 0
        
        # Inicializar con las aristas directas
        for nodo_i in self.grafo:
            i = indice[nodo_i]
            for nodo_j, peso in self.grafo[nodo_i].items():
                j = indice[nodo_j]
                distancias[i][j] = peso
                siguiente[i][j] = nodo_j
        
        # Guardar matriz inicial
        matriz_inicial = [fila[:] for fila in distancias]
        
        # Algoritmo principal
        iteraciones = []
        for k in range(n):
            cambios = []
            for i in range(n):
                for j in range(n):
                    if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                        nueva_dist = distancias[i][k] + distancias[k][j]
                        cambios.append((nodos[i], nodos[j], distancias[i][j], nueva_dist, nodos[k]))
                        distancias[i][j] = nueva_dist
                        siguiente[i][j] = siguiente[i][k]
            
            iteraciones.append((nodos[k], cambios[:]))
        
        return distancias, siguiente, nodos, indice, matriz_inicial, iteraciones
    
    def reconstruir_camino(self, siguiente, nodos, indice, inicio, destino):
        if siguiente[indice[inicio]][indice[destino]] is None:
            return []
        
        camino = [inicio]
        while inicio != destino:
            inicio = siguiente[indice[inicio]][indice[destino]]
            camino.append(inicio)
        
        return camino
    
    def imprimir_matriz(self, texto, matriz, nodos, titulo):
        texto.insert(tk.END, f"\n{titulo}:\n")
        texto.insert(tk.END, "      ")
        for nodo in nodos:
            texto.insert(tk.END, f"{nodo:>8}")
        texto.insert(tk.END, "\n")
        
        for i, nodo_i in enumerate(nodos):
            texto.insert(tk.END, f"{nodo_i:>5} ")
            for j in range(len(nodos)):
                valor = matriz[i][j]
                if valor == float('inf'):
                    texto.insert(tk.END, f"{'INF':>8}")
                else:
                    texto.insert(tk.END, f"{valor:>8.1f}")
            texto.insert(tk.END, "\n")
    
    def ejecutar_floyd(self):
        if not self.grafo:
            messagebox.showerror("Error", "El grafo está vacío. Agregue aristas primero.")
            return
        
        resultado = self.floyd_warshall()
        distancias, siguiente, nodos, indice, matriz_inicial, iteraciones = resultado
        
        # Mostrar resultados
        self.texto_resultado.delete(1.0, tk.END)
        
        # Encabezado
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "ALGORITMO DE FLOYD-WARSHALL\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        
        # Matriz inicial
        self.imprimir_matriz(self.texto_resultado, matriz_inicial, nodos, 
                            "\nMATRIZ INICIAL (Distancias directas)")
        
        # Proceso de iteraciones
        self.texto_resultado.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "PROCESO DE EJECUCIÓN:\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        
        for k, cambios in iteraciones:
            self.texto_resultado.insert(tk.END, f"\nNodo intermedio: {k}\n")
            if cambios:
                for origen, destino, dist_anterior, dist_nueva, intermedio in cambios:
                    self.texto_resultado.insert(tk.END, 
                        f"  {origen} -> {destino}: {dist_anterior:.1f} => {dist_nueva:.1f} (vía {intermedio})\n")
            else:
                self.texto_resultado.insert(tk.END, "  No se encontraron mejoras\n")
        
        # Matriz final
        self.imprimir_matriz(self.texto_resultado, distancias, nodos, 
                            "\nMATRIZ FINAL (Todas las distancias mínimas)")
        
        # Caminos específicos
        self.texto_resultado.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "CAMINOS MÁS CORTOS:\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        
        for i, nodo_i in enumerate(nodos):
            for j, nodo_j in enumerate(nodos):
                if i != j:
                    distancia = distancias[i][j]
                    if distancia != float('inf'):
                        camino = self.reconstruir_camino(siguiente, nodos, indice, nodo_i, nodo_j)
                        if camino:
                            camino_str = ' -> '.join(camino)
                            self.texto_resultado.insert(tk.END, 
                                f"{camino_str} (distancia: {distancia:.1f})\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = FloydWarshallApp(root)
    root.mainloop()