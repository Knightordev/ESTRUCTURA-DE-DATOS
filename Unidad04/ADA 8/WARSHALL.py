import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class WarshallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de Warshall - Visualizador")
        self.root.geometry("950x750")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.grafo = {}
        
        # Configurar interfaz
        self.setup_ui()
        self.cargar_grafo_ejemplo()
        
    def setup_ui(self):
        # Título
        titulo = tk.Label(self.root, text="Algoritmo de Warshall (Clausura Transitiva)", 
                         font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=10)
        
        # Subtítulo
        subtitulo = tk.Label(self.root, text="Determina si existe un camino entre cada par de nodos", 
                            font=('Arial', 11, 'italic'), bg='#f0f0f0', fg='#7f8c8d')
        subtitulo.pack(pady=2)
        
        # Frame para entrada de datos
        frame_entrada = tk.LabelFrame(self.root, text="Configuración del Grafo", 
                                     font=('Arial', 12, 'bold'), bg='#f0f0f0', padx=10, pady=10)
        frame_entrada.pack(padx=20, pady=10, fill='x')
        
        # Entrada de aristas
        tk.Label(frame_entrada, text="Agregar Arista Dirigida (Formato: A B):", 
                bg='#f0f0f0', font=('Arial', 10)).grid(row=0, column=0, sticky='w', pady=5)
        
        self.entry_arista = tk.Entry(frame_entrada, width=30, font=('Arial', 10))
        self.entry_arista.grid(row=0, column=1, padx=5, pady=5)
        
        btn_agregar = tk.Button(frame_entrada, text="Agregar Arista", 
                               command=self.agregar_arista, bg='#3498db', fg='white',
                               font=('Arial', 10, 'bold'), cursor='hand2')
        btn_agregar.grid(row=0, column=2, padx=5, pady=5)
        
        # Nota
        nota = tk.Label(frame_entrada, text="Nota: Solo se necesita el origen y destino (sin peso)", 
                       bg='#f0f0f0', font=('Arial', 9, 'italic'), fg='#7f8c8d')
        nota.grid(row=1, column=0, columnspan=3, pady=5)
        
        # Botones de acción
        frame_botones = tk.Frame(frame_entrada, bg='#f0f0f0')
        frame_botones.grid(row=2, column=0, columnspan=3, pady=10)
        
        btn_ejecutar = tk.Button(frame_botones, text="Ejecutar Warshall", 
                                command=self.ejecutar_warshall, bg='#27ae60', fg='white',
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
            if len(entrada) != 2:
                raise ValueError("Formato incorrecto")
            
            nodo1, nodo2 = entrada[0], entrada[1]
            
            # Agregar arista dirigida
            if nodo1 not in self.grafo:
                self.grafo[nodo1] = []
            
            if nodo2 not in self.grafo[nodo1]:
                self.grafo[nodo1].append(nodo2)
            
            # Asegurar que nodo2 existe en el grafo
            if nodo2 not in self.grafo:
                self.grafo[nodo2] = []
            
            self.entry_arista.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Arista agregada: {nodo1} -> {nodo2}")
            self.mostrar_grafo_actual()
            
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Use: Nodo1 Nodo2\nEjemplo: A B")
    
    def cargar_grafo_ejemplo(self):
        self.grafo = {
            'A': ['B', 'C'],
            'B': ['D'],
            'C': ['D', 'E'],
            'D': ['E'],
            'E': ['A']
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
                vecinos = ', '.join(self.grafo[nodo])
                self.texto_resultado.insert(tk.END, f"{nodo} -> {vecinos}\n")
            else:
                self.texto_resultado.insert(tk.END, f"{nodo} -> (sin aristas salientes)\n")
    
    def warshall(self):
        nodos = list(self.grafo.keys())
        n = len(nodos)
        indice = {nodo: i for i, nodo in enumerate(nodos)}
        
        # Inicializar matriz de alcanzabilidad
        alcanzabilidad = [[False] * n for _ in range(n)]
        
        # Un nodo siempre es alcanzable desde sí mismo
        for i in range(n):
            alcanzabilidad[i][i] = True
        
        # Marcar las aristas directas como alcanzables
        for nodo_i in self.grafo:
            i = indice[nodo_i]
            for nodo_j in self.grafo[nodo_i]:
                j = indice[nodo_j]
                alcanzabilidad[i][j] = True
        
        # Guardar matriz inicial
        matriz_inicial = [fila[:] for fila in alcanzabilidad]
        
        # Algoritmo principal de Warshall
        iteraciones = []
        for k in range(n):
            cambios = []
            for i in range(n):
                for j in range(n):
                    if alcanzabilidad[i][k] and alcanzabilidad[k][j]:
                        if not alcanzabilidad[i][j]:
                            alcanzabilidad[i][j] = True
                            cambios.append((nodos[i], nodos[j], nodos[k]))
            
            iteraciones.append((nodos[k], cambios[:]))
        
        return alcanzabilidad, nodos, indice, matriz_inicial, iteraciones
    
    def imprimir_matriz_booleana(self, texto, matriz, nodos, titulo):
        texto.insert(tk.END, f"\n{titulo}:\n")
        texto.insert(tk.END, "      ")
        for nodo in nodos:
            texto.insert(tk.END, f"{nodo:>4}")
        texto.insert(tk.END, "\n")
        
        for i, nodo_i in enumerate(nodos):
            texto.insert(tk.END, f"{nodo_i:>5} ")
            for j in range(len(nodos)):
                texto.insert(tk.END, f"{'1' if matriz[i][j] else '0':>4}")
            texto.insert(tk.END, "\n")
    
    def analizar_conexiones(self, texto, alcanzabilidad, nodos, indice):
        n = len(nodos)
        
        texto.insert(tk.END, "\n" + "=" * 80 + "\n")
        texto.insert(tk.END, "ANÁLISIS DE CONECTIVIDAD:\n")
        texto.insert(tk.END, "=" * 80 + "\n")
        
        # Verificar si el grafo es fuertemente conexo
        fuertemente_conexo = all(alcanzabilidad[i][j] for i in range(n) for j in range(n))
        texto.insert(tk.END, f"\n¿Grafo fuertemente conexo? {'SÍ' if fuertemente_conexo else 'NO'}\n")
        
        # Mostrar nodos alcanzables desde cada nodo
        texto.insert(tk.END, "\nNodos alcanzables desde cada nodo:\n")
        texto.insert(tk.END, "-" * 80 + "\n")
        for i, nodo_i in enumerate(nodos):
            alcanzables = [nodos[j] for j in range(n) if alcanzabilidad[i][j] and i != j]
            if alcanzables:
                texto.insert(tk.END, f"  {nodo_i}: {', '.join(alcanzables)}\n")
            else:
                texto.insert(tk.END, f"  {nodo_i}: (solo a sí mismo)\n")
        
        # Mostrar nodos que pueden llegar a cada nodo
        texto.insert(tk.END, "\nNodos que pueden llegar a cada nodo:\n")
        texto.insert(tk.END, "-" * 80 + "\n")
        for j, nodo_j in enumerate(nodos):
            pueden_llegar = [nodos[i] for i in range(n) if alcanzabilidad[i][j] and i != j]
            if pueden_llegar:
                texto.insert(tk.END, f"  {nodo_j}: {', '.join(pueden_llegar)}\n")
            else:
                texto.insert(tk.END, f"  {nodo_j}: (solo desde sí mismo)\n")
    
    def ejecutar_warshall(self):
        if not self.grafo:
            messagebox.showerror("Error", "El grafo está vacío. Agregue aristas primero.")
            return
        
        resultado = self.warshall()
        alcanzabilidad, nodos, indice, matriz_inicial, iteraciones = resultado
        
        # Mostrar resultados
        self.texto_resultado.delete(1.0, tk.END)
        
        # Encabezado
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "ALGORITMO DE WARSHALL - CLAUSURA TRANSITIVA\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        
        # Matriz inicial
        self.imprimir_matriz_booleana(self.texto_resultado, matriz_inicial, nodos, 
                                      "\nMATRIZ DE ADYACENCIA INICIAL (Aristas directas)")
        
        # Proceso de iteraciones
        self.texto_resultado.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "PROCESO DE EJECUCIÓN:\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        
        for k, cambios in iteraciones:
            self.texto_resultado.insert(tk.END, f"\nIteración: Nodo intermedio '{k}'\n")
            if cambios:
                for origen, destino, intermedio in cambios:
                    self.texto_resultado.insert(tk.END, 
                        f"  Nuevo camino: {origen} -> {destino} (vía {intermedio})\n")
            else:
                self.texto_resultado.insert(tk.END, "  No se encontraron nuevos caminos\n")
        
        # Matriz final
        self.imprimir_matriz_booleana(self.texto_resultado, alcanzabilidad, nodos, 
                                      "\nMATRIZ DE CLAUSURA TRANSITIVA (Todos los caminos)")
        
        # Análisis de conexiones
        self.analizar_conexiones(self.texto_resultado, alcanzabilidad, nodos, indice)
        
        # Verificación de caminos específicos
        self.texto_resultado.insert(tk.END, "\n" + "=" * 80 + "\n")
        self.texto_resultado.insert(tk.END, "VERIFICACIÓN DE CAMINOS:\n")
        self.texto_resultado.insert(tk.END, "=" * 80 + "\n")
        
        for i, nodo_i in enumerate(nodos):
            for j, nodo_j in enumerate(nodos):
                if i != j:
                    existe = alcanzabilidad[i][j]
                    simbolo = "✓" if existe else "✗"
                    self.texto_resultado.insert(tk.END, 
                        f"{simbolo} {nodo_i} -> {nodo_j}: {'Existe camino' if existe else 'No hay camino'}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = WarshallApp(root)
    root.mainloop()