import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import math

class Arista:
    """Representa una arista en el grafo"""
    def __init__(self, origen, destino, objeto, dirigida=False):
        self.origen = origen
        self.destino = destino
        self.objeto = objeto
        self.dirigida = dirigida
    
    def __repr__(self):
        if self.dirigida:
            return f"{self.origen} -> {self.destino} ({self.objeto})"
        return f"{self.origen} -- {self.destino} ({self.objeto})"


class Grafo:
    """Tipo de Dato Abstracto Grafo"""
    
    def __init__(self):
        self.vertices = {}
        self.aristas = []
        self.siguiente_vertice = 0
        self.posiciones = {}  # Posiciones visuales de los vértices
    
    # ==================== OPERACIONES GENERALES ====================
    
    def numVertices(self):
        return len(self.vertices)
    
    def numAristas(self):
        return len(self.aristas)
    
    def vertices_lista(self):
        return list(self.vertices.keys())
    
    def aristas_lista(self):
        return list(range(len(self.aristas)))
    
    def grado(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        grado = 0
        for arista in self.aristas:
            if not arista.dirigida:
                if arista.origen == v or arista.destino == v:
                    grado += 1
            else:
                if arista.origen == v or arista.destino == v:
                    grado += 1
        return grado
    
    def verticesAdyacentes(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        adyacentes = set()
        for arista in self.aristas:
            if arista.origen == v:
                adyacentes.add(arista.destino)
            if arista.destino == v:
                if not arista.dirigida:
                    adyacentes.add(arista.origen)
        return list(adyacentes)
    
    def aristasIncidentes(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        incidentes = []
        for i, arista in enumerate(self.aristas):
            if arista.origen == v or arista.destino == v:
                incidentes.append(i)
        return incidentes
    
    def verticesFinales(self, e):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        arista = self.aristas[e]
        return [arista.origen, arista.destino]
    
    def opuesto(self, v, e):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        arista = self.aristas[e]
        if arista.origen == v:
            return arista.destino
        elif arista.destino == v:
            return arista.origen
        else:
            raise ValueError(f"La arista {e} no es incidente al vértice {v}")
    
    def esAdyacente(self, v, w):
        if v not in self.vertices or w not in self.vertices:
            return False
        for arista in self.aristas:
            if (arista.origen == v and arista.destino == w):
                return True
            if not arista.dirigida and (arista.origen == w and arista.destino == v):
                return True
        return False
    
    # ==================== OPERACIONES CON ARISTAS DIRIGIDAS ====================
    
    def aristasDirigidas(self):
        return [i for i, arista in enumerate(self.aristas) if arista.dirigida]
    
    def aristasNodirigidas(self):
        return [i for i, arista in enumerate(self.aristas) if not arista.dirigida]
    
    def gradoEnt(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        grado = 0
        for arista in self.aristas:
            if arista.dirigida and arista.destino == v:
                grado += 1
        return grado
    
    def gradoSalida(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        grado = 0
        for arista in self.aristas:
            if arista.dirigida and arista.origen == v:
                grado += 1
        return grado
    
    def aristasIncidentesEnt(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        return [i for i, arista in enumerate(self.aristas) 
                if arista.dirigida and arista.destino == v]
    
    def aristasIncidentesSal(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        return [i for i, arista in enumerate(self.aristas) 
                if arista.dirigida and arista.origen == v]
    
    def verticesAdyacentesEnt(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        return [arista.origen for arista in self.aristas 
                if arista.dirigida and arista.destino == v]
    
    def verticesAdyacentesSal(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        return [arista.destino for arista in self.aristas 
                if arista.dirigida and arista.origen == v]
    
    def destino(self, e):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        if not self.aristas[e].dirigida:
            raise ValueError(f"La arista {e} no es dirigida")
        return self.aristas[e].destino
    
    def origen(self, e):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        if not self.aristas[e].dirigida:
            raise ValueError(f"La arista {e} no es dirigida")
        return self.aristas[e].origen
    
    def esDirigida(self, e):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        return self.aristas[e].dirigida
    
    # ==================== OPERACIONES PARA ACTUALIZAR GRAFOS ====================
    
    def insertaArista(self, v, w, o):
        if v not in self.vertices or w not in self.vertices:
            raise ValueError("Ambos vértices deben existir")
        arista = Arista(v, w, o, dirigida=False)
        self.aristas.append(arista)
        return len(self.aristas) - 1
    
    def insertaAristaDirigida(self, v, w, o):
        if v not in self.vertices or w not in self.vertices:
            raise ValueError("Ambos vértices deben existir")
        arista = Arista(v, w, o, dirigida=True)
        self.aristas.append(arista)
        return len(self.aristas) - 1
    
    def insertaVertice(self, o, x=None, y=None):
        indice = self.siguiente_vertice
        self.vertices[indice] = o
        if x is not None and y is not None:
            self.posiciones[indice] = (x, y)
        self.siguiente_vertice += 1
        return indice
    
    def eliminaVertice(self, v):
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        self.aristas = [arista for arista in self.aristas 
                       if arista.origen != v and arista.destino != v]
        del self.vertices[v]
        if v in self.posiciones:
            del self.posiciones[v]
    
    def eliminaArista(self, e):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        del self.aristas[e]
    
    def convierteNodirigida(self, e):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        self.aristas[e].dirigida = False
    
    def invierteDireccion(self, e):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        if not self.aristas[e].dirigida:
            raise ValueError(f"La arista {e} no es dirigida")
        arista = self.aristas[e]
        arista.origen, arista.destino = arista.destino, arista.origen
    
    def asignaDireccionDesde(self, e, v):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        arista = self.aristas[e]
        if arista.origen != v and arista.destino != v:
            raise ValueError(f"La arista {e} no es incidente al vértice {v}")
        if arista.destino == v:
            arista.origen, arista.destino = arista.destino, arista.origen
        arista.dirigida = True
    
    def asignaDireccionA(self, e, v):
        if e < 0 or e >= len(self.aristas):
            raise ValueError(f"La arista {e} no existe")
        if v not in self.vertices:
            raise ValueError(f"El vértice {v} no existe")
        arista = self.aristas[e]
        if arista.origen != v and arista.destino != v:
            raise ValueError(f"La arista {e} no es incidente al vértice {v}")
        if arista.origen == v:
            arista.origen, arista.destino = arista.destino, arista.origen
        arista.dirigida = True


class GrafoGUI:
    """Interfaz gráfica para el TDA Grafo"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("TDA Grafo - Visualizador Interactivo")
        self.root.geometry("1200x700")
        
        self.grafo = Grafo()
        self.vertice_seleccionado = None
        self.primer_vertice_arista = None
        self.radio_vertice = 25
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame izquierdo - Canvas
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Canvas para dibujar el grafo
        self.canvas = tk.Canvas(left_frame, bg="white", width=700, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.canvas_click)
        self.canvas.bind("<Button-3>", self.canvas_right_click)
        
        # Frame derecho - Controles
        right_frame = ttk.Frame(main_frame, width=400)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        right_frame.pack_propagate(False)
        
        # Título
        ttk.Label(right_frame, text="Panel de Control", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Modo de grafo
        mode_frame = ttk.LabelFrame(right_frame, text="Tipo de Grafo", padding=10)
        mode_frame.pack(fill=tk.X, pady=5)
        
        self.modo_dirigido = tk.BooleanVar(value=False)
        ttk.Radiobutton(mode_frame, text="No Dirigido", variable=self.modo_dirigido, 
                       value=False).pack(anchor=tk.W)
        ttk.Radiobutton(mode_frame, text="Dirigido", variable=self.modo_dirigido, 
                       value=True).pack(anchor=tk.W)
        
        # Operaciones con vértices
        vertex_frame = ttk.LabelFrame(right_frame, text="Operaciones con Vértices", padding=10)
        vertex_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(vertex_frame, text="Agregar Vértice (Click en Canvas)", 
                  command=self.info_agregar_vertice).pack(fill=tk.X, pady=2)
        ttk.Button(vertex_frame, text="Eliminar Vértice Seleccionado", 
                  command=self.eliminar_vertice).pack(fill=tk.X, pady=2)
        ttk.Button(vertex_frame, text="Info Vértice Seleccionado", 
                  command=self.info_vertice).pack(fill=tk.X, pady=2)
        
        # Operaciones con aristas
        edge_frame = ttk.LabelFrame(right_frame, text="Operaciones con Aristas", padding=10)
        edge_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(edge_frame, text="Click en 2 vértices para crear arista").pack()
        ttk.Button(edge_frame, text="Convertir Arista a No Dirigida", 
                  command=self.convertir_no_dirigida).pack(fill=tk.X, pady=2)
        ttk.Button(edge_frame, text="Invertir Dirección de Arista", 
                  command=self.invertir_direccion).pack(fill=tk.X, pady=2)
        ttk.Button(edge_frame, text="Eliminar Arista", 
                  command=self.eliminar_arista).pack(fill=tk.X, pady=2)
        
        # Información del grafo
        info_frame = ttk.LabelFrame(right_frame, text="Información del Grafo", padding=10)
        info_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.info_text = tk.Text(info_frame, height=15, width=40)
        self.info_text.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(info_frame, orient=tk.VERTICAL, command=self.info_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.info_text.config(yscrollcommand=scrollbar.set)
        
        # Botones de acción
        action_frame = ttk.Frame(right_frame)
        action_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(action_frame, text="Actualizar Info", 
                  command=self.actualizar_info).pack(fill=tk.X, pady=2)
        ttk.Button(action_frame, text="Limpiar Grafo", 
                  command=self.limpiar_grafo).pack(fill=tk.X, pady=2)
        
        self.actualizar_info()
    
    def info_agregar_vertice(self):
        messagebox.showinfo("Agregar Vértice", 
                          "Haz click izquierdo en el canvas para agregar un vértice")
    
    def canvas_click(self, event):
        x, y = event.x, event.y
        
        # Verificar si se hizo click en un vértice existente
        vertice_clickeado = self.obtener_vertice_en_posicion(x, y)
        
        if vertice_clickeado is not None:
            # Seleccionar vértice para crear arista
            if self.primer_vertice_arista is None:
                self.primer_vertice_arista = vertice_clickeado
                self.vertice_seleccionado = vertice_clickeado
                messagebox.showinfo("Vértice Seleccionado", 
                                  f"Vértice {vertice_clickeado} seleccionado. "
                                  f"Click en otro vértice para crear arista.")
            else:
                if self.primer_vertice_arista != vertice_clickeado:
                    self.crear_arista(self.primer_vertice_arista, vertice_clickeado)
                self.primer_vertice_arista = None
        else:
            # Crear nuevo vértice
            etiqueta = simpledialog.askstring("Nuevo Vértice", 
                                             "Ingrese la etiqueta del vértice:")
            if etiqueta:
                v = self.grafo.insertaVertice(etiqueta, x, y)
                self.dibujar_grafo()
                self.actualizar_info()
    
    def canvas_right_click(self, event):
        x, y = event.x, event.y
        vertice = self.obtener_vertice_en_posicion(x, y)
        
        if vertice is not None:
            self.vertice_seleccionado = vertice
            self.actualizar_info()
    
    def obtener_vertice_en_posicion(self, x, y):
        for v, (vx, vy) in self.grafo.posiciones.items():
            distancia = math.sqrt((x - vx)**2 + (y - vy)**2)
            if distancia <= self.radio_vertice:
                return v
        return None
    
    def crear_arista(self, v1, v2):
        peso = simpledialog.askstring("Nueva Arista", 
                                     f"Peso de la arista {v1} -> {v2}:",
                                     initialvalue="1")
        if peso:
            try:
                if self.modo_dirigido.get():
                    self.grafo.insertaAristaDirigida(v1, v2, peso)
                else:
                    self.grafo.insertaArista(v1, v2, peso)
                self.dibujar_grafo()
                self.actualizar_info()
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def eliminar_vertice(self):
        if self.vertice_seleccionado is None:
            messagebox.showwarning("Advertencia", "Seleccione un vértice primero")
            return
        
        try:
            self.grafo.eliminaVertice(self.vertice_seleccionado)
            self.vertice_seleccionado = None
            self.dibujar_grafo()
            self.actualizar_info()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def info_vertice(self):
        if self.vertice_seleccionado is None:
            messagebox.showwarning("Advertencia", "Seleccione un vértice primero")
            return
        
        v = self.vertice_seleccionado
        try:
            info = f"Vértice: {v}\n"
            info += f"Etiqueta: {self.grafo.vertices[v]}\n"
            info += f"Grado: {self.grafo.grado(v)}\n"
            info += f"Adyacentes: {self.grafo.verticesAdyacentes(v)}\n"
            info += f"Aristas incidentes: {self.grafo.aristasIncidentes(v)}\n"
            
            if self.modo_dirigido.get():
                info += f"Grado entrada: {self.grafo.gradoEnt(v)}\n"
                info += f"Grado salida: {self.grafo.gradoSalida(v)}\n"
            
            messagebox.showinfo("Información del Vértice", info)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def convertir_no_dirigida(self):
        arista_idx = simpledialog.askinteger("Convertir Arista", 
                                            "Índice de la arista a convertir:")
        if arista_idx is not None:
            try:
                self.grafo.convierteNodirigida(arista_idx)
                self.dibujar_grafo()
                self.actualizar_info()
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def invertir_direccion(self):
        arista_idx = simpledialog.askinteger("Invertir Dirección", 
                                            "Índice de la arista a invertir:")
        if arista_idx is not None:
            try:
                self.grafo.invierteDireccion(arista_idx)
                self.dibujar_grafo()
                self.actualizar_info()
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def eliminar_arista(self):
        arista_idx = simpledialog.askinteger("Eliminar Arista", 
                                            "Índice de la arista a eliminar:")
        if arista_idx is not None:
            try:
                self.grafo.eliminaArista(arista_idx)
                self.dibujar_grafo()
                self.actualizar_info()
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def limpiar_grafo(self):
        if messagebox.askyesno("Confirmar", "¿Desea limpiar todo el grafo?"):
            self.grafo = Grafo()
            self.vertice_seleccionado = None
            self.primer_vertice_arista = None
            self.dibujar_grafo()
            self.actualizar_info()
    
    def actualizar_info(self):
        self.info_text.delete(1.0, tk.END)
        
        info = f"=== INFORMACIÓN DEL GRAFO ===\n\n"
        info += f"Tipo: {'Dirigido' if self.modo_dirigido.get() else 'No Dirigido'}\n"
        info += f"Número de vértices: {self.grafo.numVertices()}\n"
        info += f"Número de aristas: {self.grafo.numAristas()}\n\n"
        
        info += "=== VÉRTICES ===\n"
        for v in self.grafo.vertices_lista():
            marcador = " ◀" if v == self.vertice_seleccionado else ""
            info += f"[{v}] {self.grafo.vertices[v]}{marcador}\n"
        
        info += "\n=== ARISTAS ===\n"
        for i, arista in enumerate(self.grafo.aristas):
            info += f"[{i}] {arista}\n"
        
        if self.vertice_seleccionado is not None:
            info += f"\n=== VÉRTICE SELECCIONADO: {self.vertice_seleccionado} ===\n"
            try:
                v = self.vertice_seleccionado
                info += f"Grado: {self.grafo.grado(v)}\n"
                info += f"Adyacentes: {self.grafo.verticesAdyacentes(v)}\n"
            except:
                pass
        
        self.info_text.insert(1.0, info)
    
    def dibujar_grafo(self):
        self.canvas.delete("all")
        
        # Dibujar aristas
        for i, arista in enumerate(self.grafo.aristas):
            if arista.origen in self.grafo.posiciones and arista.destino in self.grafo.posiciones:
                x1, y1 = self.grafo.posiciones[arista.origen]
                x2, y2 = self.grafo.posiciones[arista.destino]
                
                color = "blue" if arista.dirigida else "black"
                
                if arista.dirigida:
                    # Calcular punto de flecha
                    dx = x2 - x1
                    dy = y2 - y1
                    distancia = math.sqrt(dx**2 + dy**2)
                    if distancia > 0:
                        dx /= distancia
                        dy /= distancia
                        x2_ajustado = x2 - dx * self.radio_vertice
                        y2_ajustado = y2 - dy * self.radio_vertice
                        
                        self.canvas.create_line(x1, y1, x2_ajustado, y2_ajustado, 
                                              fill=color, width=2, arrow=tk.LAST, 
                                              arrowshape=(10, 12, 5))
                else:
                    self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
                
                # Etiqueta de la arista
                mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(mid_x, mid_y - 10, text=f"[{i}]{arista.objeto}", 
                                      font=("Arial", 9), fill="red")
        
        # Dibujar vértices
        for v, (x, y) in self.grafo.posiciones.items():
            color = "yellow" if v == self.vertice_seleccionado else "lightblue"
            self.canvas.create_oval(x - self.radio_vertice, y - self.radio_vertice,
                                   x + self.radio_vertice, y + self.radio_vertice,
                                   fill=color, outline="black", width=2)
            self.canvas.create_text(x, y, text=f"{v}\n{self.grafo.vertices[v]}", 
                                   font=("Arial", 10, "bold"))


if __name__ == "__main__":
    root = tk.Tk()
    app = GrafoGUI(root)
    root.mainloop()