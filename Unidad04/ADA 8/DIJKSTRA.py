import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import heapq
from collections import defaultdict

class DijkstraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de Dijkstra - Visualizador")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.grafo = {}
        self.nodo_inicio = tk.StringVar(value="A")
        
        # Configurar interfaz
        self.setup_ui()
        self.cargar_grafo_ejemplo()
        
    def setup_ui(self):
        # Título
        titulo = tk.Label(self.root, text="Algoritmo de Dijkstra", 
                         font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=10)
        
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
        
        # Nodo de inicio
        tk.Label(frame_entrada, text="Nodo de Inicio:", 
                bg='#f0f0f0', font=('Arial', 10)).grid(row=1, column=0, sticky='w', pady=5)
        
        entry_inicio = tk.Entry(frame_entrada, textvariable=self.nodo_inicio, 
                               width=10, font=('Arial', 10))
        entry_inicio.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        
        # Botones de acción
        frame_botones = tk.Frame(frame_entrada, bg='#f0f0f0')
        frame_botones.grid(row=2, column=0, columnspan=3, pady=10)
        
        btn_ejecutar = tk.Button(frame_botones, text="Ejecutar Dijkstra", 
                                command=self.ejecutar_dijkstra, bg='#27ae60', fg='white',
                                font=('Arial', 11, 'bold'), cursor='hand2', width=15)
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
                                                         width=80, height=20, 
                                                         font=('Courier', 10), 
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
                messagebox.showerror("Error", "El peso debe ser positivo para Dijkstra")
                return
            
            # Agregar arista bidireccional
            if nodo1 not in self.grafo:
                self.grafo[nodo1] = []
            if nodo2 not in self.grafo:
                self.grafo[nodo2] = []
            
            self.grafo[nodo1].append((nodo2, peso))
            self.grafo[nodo2].append((nodo1, peso))
            
            self.entry_arista.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Arista agregada: {nodo1} <-> {nodo2} (peso: {peso})")
            self.mostrar_grafo_actual()
            
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Use: Nodo1 Nodo2 Peso\nEjemplo: A B 5")
    
    def cargar_grafo_ejemplo(self):
        self.grafo = {
            'A': [('B', 4), ('C', 2)],
            'B': [('A', 4), ('C', 1), ('D', 5)],
            'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
            'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
            'E': [('C', 10), ('D', 2), ('F', 3)],
            'F': [('D', 6), ('E', 3)]
        }
        self.mostrar_grafo_actual()
        messagebox.showinfo("Éxito", "Grafo de ejemplo cargado correctamente")
    
    def limpiar_grafo(self):
        self.grafo = {}
        self.texto_resultado.delete(1.0, tk.END)
        messagebox.showinfo("Éxito", "Grafo limpiado")
    
    def mostrar_grafo_actual(self):
        self.texto_resultado.delete(1.0, tk.END)
        self.texto_resultado.insert(tk.END, "=" * 70 + "\n")
        self.texto_resultado.insert(tk.END, "GRAFO ACTUAL\n")
        self.texto_resultado.insert(tk.END, "=" * 70 + "\n\n")
        
        for nodo in sorted(self.grafo.keys()):
            vecinos = ', '.join([f"{v}({p})" for v, p in self.grafo[nodo]])
            self.texto_resultado.insert(tk.END, f"{nodo} -> {vecinos}\n")
    
    def dijkstra(self, inicio):
        if inicio not in self.grafo:
            return None, None
        
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0
        predecesores = {nodo: None for nodo in self.grafo}
        
        cola_prioridad = [(0, inicio)]
        visitados = set()
        proceso = []
        
        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
            
            if nodo_actual in visitados:
                continue
            
            visitados.add(nodo_actual)
            proceso.append(f"Visitando nodo: {nodo_actual} (distancia: {distancia_actual})")
            
            for vecino, peso in self.grafo[nodo_actual]:
                distancia = distancia_actual + peso
                
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    predecesores[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (distancia, vecino))
                    proceso.append(f"  Actualizando {vecino}: distancia = {distancia}")
        
        return distancias, predecesores, proceso
    
    def reconstruir_camino(self, predecesores, inicio, destino):
        camino = []
        nodo_actual = destino
        
        while nodo_actual is not None:
            camino.append(nodo_actual)
            nodo_actual = predecesores[nodo_actual]
        
        camino.reverse()
        
        if camino[0] == inicio:
            return camino
        else:
            return []
    
    def ejecutar_dijkstra(self):
        inicio = self.nodo_inicio.get().strip()
        
        if not self.grafo:
            messagebox.showerror("Error", "El grafo está vacío. Agregue aristas primero.")
            return
        
        if inicio not in self.grafo:
            messagebox.showerror("Error", f"El nodo '{inicio}' no existe en el grafo.")
            return
        
        resultado = self.dijkstra(inicio)
        if resultado[0] is None:
            messagebox.showerror("Error", "Error al ejecutar el algoritmo")
            return
        
        distancias, predecesores, proceso = resultado
        
        # Mostrar resultados
        self.texto_resultado.delete(1.0, tk.END)
        
        # Encabezado
        self.texto_resultado.insert(tk.END, "=" * 70 + "\n")
        self.texto_resultado.insert(tk.END, f"ALGORITMO DE DIJKSTRA - Nodo inicial: {inicio}\n")
        self.texto_resultado.insert(tk.END, "=" * 70 + "\n\n")
        
        # Proceso
        self.texto_resultado.insert(tk.END, "PROCESO DE EJECUCIÓN:\n")
        self.texto_resultado.insert(tk.END, "-" * 70 + "\n")
        for paso in proceso:
            self.texto_resultado.insert(tk.END, paso + "\n")
        
        # Distancias
        self.texto_resultado.insert(tk.END, "\n" + "=" * 70 + "\n")
        self.texto_resultado.insert(tk.END, "DISTANCIAS MÍNIMAS:\n")
        self.texto_resultado.insert(tk.END, "=" * 70 + "\n")
        for nodo in sorted(distancias.keys()):
            dist = distancias[nodo]
            if dist == float('inf'):
                self.texto_resultado.insert(tk.END, f"{inicio} -> {nodo}: INALCANZABLE\n")
            else:
                self.texto_resultado.insert(tk.END, f"{inicio} -> {nodo}: {dist}\n")
        
        # Caminos
        self.texto_resultado.insert(tk.END, "\n" + "=" * 70 + "\n")
        self.texto_resultado.insert(tk.END, "CAMINOS MÁS CORTOS:\n")
        self.texto_resultado.insert(tk.END, "=" * 70 + "\n")
        for nodo in sorted(self.grafo.keys()):
            if nodo != inicio:
                camino = self.reconstruir_camino(predecesores, inicio, nodo)
                if camino:
                    camino_str = ' -> '.join(camino)
                    self.texto_resultado.insert(tk.END, 
                        f"{camino_str} (distancia: {distancias[nodo]})\n")
                else:
                    self.texto_resultado.insert(tk.END, 
                        f"{inicio} -> {nodo}: No hay camino\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DijkstraApp(root)
    root.mainloop()