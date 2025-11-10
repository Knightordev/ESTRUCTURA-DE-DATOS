import tkinter as tk
from tkinter import messagebox, Canvas

class Grafo:
    def __init__(self):
        # Grafo no dirigido con pesos
        self.grafo = {
            "Chihuahua": [("Sonora", 220), ("Coahuila", 310), ("Durango", 280)],
            "Sonora": [("Chihuahua", 220), ("Sinaloa", 190), ("Durango", 260)],
            "Coahuila": [("Chihuahua", 310), ("Nuevo León", 140), ("Durango", 230), ("Tamaulipas", 180)],
            "Nuevo León": [("Coahuila", 140), ("Tamaulipas", 110)],
            "Tamaulipas": [("Nuevo León", 110), ("Coahuila", 180)],
            "Durango": [("Chihuahua", 280), ("Sonora", 260), ("Sinaloa", 200), ("Coahuila", 230)],
            "Sinaloa": [("Sonora", 190), ("Durango", 200)],
        }

    # -------- OPERACIONES GENERALES ----------
    def numVertices(self):
        return len(self.grafo)

    def numAristas(self):
        total = sum(len(v) for v in self.grafo.values()) // 2
        return total

    def vertices_lista(self):
        return list(self.grafo.keys())

    def aristas_lista(self):
        aristas = []
        for v in self.grafo:
            for w, c in self.grafo[v]:
                if (w, v, c) not in aristas:
                    aristas.append((v, w, c))
        return aristas

    def grado(self, v):
        return len(self.grafo[v])

    def verticesAdyacentes(self, v):
        return [x[0] for x in self.grafo[v]]

    def aristasIncidentes(self, v):
        return [(v, w, c) for w, c in self.grafo[v]]

    def verticesFinales(self, e):
        return e[0], e[1]

    def opuesto(self, v, e):
        return e[1] if e[0] == v else e[0]

    def esAdyacente(self, v, w):
        return any(x[0] == w for x in self.grafo[v])

    # -------- RECORRIDOS ----------
    def recorrido_sin_repetir(self, inicio):
        """Recorrido simple DFS visitando todos los estados sin repetir"""
        visitados = []
        costo_total = 0

        def dfs(v):
            nonlocal costo_total
            visitados.append(v)
            for w, c in self.grafo[v]:
                if w not in visitados:
                    costo_total += c
                    dfs(w)

        dfs(inicio)
        return visitados, costo_total

    def recorrido_con_repetir(self, inicio):
        """Recorrido visitando los 7 estados, repitiendo solo uno"""
        recorrido, costo = self.recorrido_sin_repetir(inicio)

        # Repetimos solo un estado (por ejemplo, el segundo)
        if len(recorrido) >= 2:
            estado_repetido = recorrido[1]
            recorrido_con_repetido = recorrido.copy()
            recorrido_con_repetido.insert(3, estado_repetido)  # lo repite una vez
            costo_extra = None

            # Buscar costo entre el nodo anterior y el repetido
            anterior = recorrido_con_repetido[2]
            for w, c in self.grafo[anterior]:
                if w == estado_repetido:
                    costo_extra = c
                    break
            if costo_extra is None:
                costo_extra = 0

            costo_total = costo + costo_extra
            return recorrido_con_repetido, costo_total
        else:
            return recorrido, costo

    # -------- VISUALIZACIÓN EN TKINTER ----------
    def dibujar(self, canvas):
        canvas.delete("all")
        posiciones = {
            "Chihuahua": (100, 100),
            "Sonora": (150, 250),
            "Coahuila": (300, 100),
            "Nuevo León": (400, 180),
            "Tamaulipas": (480, 300),
            "Durango": (220, 200),
            "Sinaloa": (200, 320),
        }

        # Dibujar aristas
        for v in self.grafo:
            x1, y1 = posiciones[v]
            for w, c in self.grafo[v]:
                x2, y2 = posiciones[w]
                canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)
                canvas.create_text((x1 + x2)//2, (y1 + y2)//2, text=str(c), fill="blue", font=("Arial", 8))

        # Dibujar vértices
        for v, (x, y) in posiciones.items():
            canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightgreen")
            canvas.create_text(x, y, text=v, font=("Arial", 8, "bold"))


# -------- INTERFAZ TKINTER ----------
def main():
    g = Grafo()
    root = tk.Tk()
    root.title("Grafo de 7 Estados de México")

    canvas = Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    # Botones
    def mostrar_info():
        info = f"""
Número de vértices: {g.numVertices()}
Número de aristas: {g.numAristas()}
Vértices: {g.vertices_lista()}
Aristas: {g.aristas_lista()}
"""
        messagebox.showinfo("Información del Grafo", info)

    def recorrido_a():
        recorrido, costo = g.recorrido_sin_repetir("Chihuahua")
        messagebox.showinfo("Recorrido sin repetir", f"Recorrido: {recorrido}\nCosto total: {costo}")

    def recorrido_b():
        recorrido, costo = g.recorrido_con_repetir("Chihuahua")
        messagebox.showinfo("Recorrido con repetir", f"Recorrido: {recorrido}\nCosto total: {costo}")

    btn1 = tk.Button(root, text="Mostrar información", command=mostrar_info)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Recorrido sin repetir", command=recorrido_a)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Recorrido con repetir", command=recorrido_b)
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Dibujar grafo", command=lambda: g.dibujar(canvas))
    btn4.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
