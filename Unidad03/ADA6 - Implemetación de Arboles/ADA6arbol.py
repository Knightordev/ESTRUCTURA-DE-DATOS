import tkinter as tk
from tkinter import messagebox
from collections import deque

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # [1] Insertar
    def insertar(self, dato):
        def _insertar(nodo, dato):
            if nodo is None:
                return Nodo(dato)
            if dato < nodo.dato:
                nodo.izq = _insertar(nodo.izq, dato)
            elif dato > nodo.dato:
                nodo.der = _insertar(nodo.der, dato)
            return nodo
        self.raiz = _insertar(self.raiz, dato)

    # [2] Buscar
    def buscar(self, dato):
        n = self.raiz
        while n:
            if dato == n.dato:
                return True
            n = n.izq if dato < n.dato else n.der
        return False

    # [3] Eliminar
    def eliminar(self, dato):
        def _minimo(n):
            while n.izq:
                n = n.izq
            return n

        def _elim(n, dato):
            if not n:
                return n
            if dato < n.dato:
                n.izq = _elim(n.izq, dato)
            elif dato > n.dato:
                n.der = _elim(n.der, dato)
            else:
                if n.izq is None:
                    return n.der
                if n.der is None:
                    return n.izq
                temp = _minimo(n.der)
                n.dato = temp.dato
                n.der = _elim(n.der, temp.dato)
            return n
        self.raiz = _elim(self.raiz, dato)

    # [4] Altura
    def altura(self):
        def _alt(n):
            if n is None:
                return 0
            return 1 + max(_alt(n.izq), _alt(n.der))
        return _alt(self.raiz)

    # [5] Contar hojas
    def contarHojas(self):
        def _hojas(n):
            if n is None:
                return 0
            if not n.izq and not n.der:
                return 1
            return _hojas(n.izq) + _hojas(n.der)
        return _hojas(self.raiz)

    # [6] Contar nodos
    def contarNodos(self):
        def _n(n):
            if n is None:
                return 0
            return 1 + _n(n.izq) + _n(n.der)
        return _n(self.raiz)

    # [7] Es completo
    def esCompleto(self):
        if not self.raiz:
            return True
        cola = deque([self.raiz])
        vacio = False
        while cola:
            n = cola.popleft()
            if n:
                if vacio:
                    return False
                cola.append(n.izq)
                cola.append(n.der)
            else:
                vacio = True
        return True

    # [8] Es lleno
    def esLleno(self):
        def _ll(n):
            if n is None:
                return True
            if (n.izq is None) != (n.der is None):
                return False
            return _ll(n.izq) and _ll(n.der)
        return _ll(self.raiz)

    # [9] Calcular grados de cada nodo
    def grados(self):
        grados_dict = {}
        def _gr(n):
            if n:
                grado = int(n.izq is not None) + int(n.der is not None)
                grados_dict[n.dato] = grado
                _gr(n.izq)
                _gr(n.der)
        _gr(self.raiz)
        return grados_dict

    # [10] Eliminar todo
    def eliminarArbol(self):
        self.raiz = None


class ArbolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Árbol Binario de Búsqueda (ABB) con grados")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f5f5f5")

        self.arbol = ArbolBinarioBusqueda()

        frame = tk.Frame(self.root, bg="#f5f5f5")
        frame.pack(pady=10)

        tk.Label(frame, text="Valor:", bg="#f5f5f5", font=("Arial", 12)).grid(row=0, column=0)
        self.entry = tk.Entry(frame, font=("Arial", 12), width=10)
        self.entry.grid(row=0, column=1, padx=5)

        tk.Button(frame, text="Insertar", command=self.insertar, bg="#81c784", font=("Arial", 11)).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Buscar", command=self.buscar, bg="#64b5f6", font=("Arial", 11)).grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Eliminar", command=self.eliminar, bg="#ffb74d", font=("Arial", 11)).grid(row=0, column=4, padx=5)
        tk.Button(frame, text="Limpiar", command=self.limpiar, bg="#e57373", font=("Arial", 11)).grid(row=0, column=5, padx=5)

        tk.Button(frame, text="Altura", command=self.altura, font=("Arial", 11)).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(frame, text="Hojas", command=self.hojas, font=("Arial", 11)).grid(row=1, column=3, padx=5, pady=5)
        tk.Button(frame, text="Nodos", command=self.nodos, font=("Arial", 11)).grid(row=1, column=4, padx=5, pady=5)
        tk.Button(frame, text="¿Completo?", command=self.completo, bg="#fff59d", font=("Arial", 11)).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(frame, text="¿Lleno?", command=self.lleno, bg="#ce93d8", font=("Arial", 11)).grid(row=2, column=3, padx=5, pady=5)
        tk.Button(frame, text="Grados", command=self.grados, bg="#90caf9", font=("Arial", 11)).grid(row=2, column=4, padx=5, pady=5)

        self.canvas = tk.Canvas(self.root, bg="white", width=950, height=500)
        self.canvas.pack(pady=10)

    def insertar(self):
        try:
            v = int(self.entry.get())
            self.entry.delete(0, tk.END)
            self.arbol.insertar(v)
            self.dibujar()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def buscar(self):
        try:
            v = int(self.entry.get())
            self.entry.delete(0, tk.END)
            msg = f"✅ El valor {v} está en el árbol." if self.arbol.buscar(v) else f"❌ El valor {v} no se encuentra."
            messagebox.showinfo("Buscar", msg)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def eliminar(self):
        try:
            v = int(self.entry.get())
            self.entry.delete(0, tk.END)
            self.arbol.eliminar(v)
            self.dibujar()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def limpiar(self):
        self.arbol.eliminarArbol()
        self.canvas.delete("all")

    def altura(self):
        h = self.arbol.altura()
        messagebox.showinfo("Altura", f"Altura del árbol: {h}")

    def hojas(self):
        h = self.arbol.contarHojas()
        messagebox.showinfo("Hojas", f"Cantidad de hojas: {h}")

    def nodos(self):
        n = self.arbol.contarNodos()
        messagebox.showinfo("Nodos", f"Cantidad total de nodos: {n}")

    def completo(self):
        es = self.arbol.esCompleto()
        messagebox.showinfo("Árbol completo", "✅ Es completo" if es else "❌ No es completo")

    def lleno(self):
        es = self.arbol.esLleno()
        messagebox.showinfo("Árbol lleno", "✅ Es lleno" if es else "❌ No es lleno")

    def grados(self):
        g = self.arbol.grados()
        texto = "\n".join([f"Nodo {k}: grado {v}" for k, v in g.items()])
        if not texto:
            texto = "Árbol vacío"
        messagebox.showinfo("Grados de los nodos", texto)

    def dibujar(self):
        self.canvas.delete("all")
        if not self.arbol.raiz:
            return

        def _dibujar(n, x, y, dx):
            if n is None:
                return
            r = 20
            if n.izq:
                self.canvas.create_line(x, y, x - dx, y + 80, width=2)
                _dibujar(n.izq, x - dx, y + 80, dx / 1.8)
            if n.der:
                self.canvas.create_line(x, y, x + dx, y + 80, width=2)
                _dibujar(n.der, x + dx, y + 80, dx / 1.8)

            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#64b5f6", outline="black", width=2)
            grado = int(n.izq is not None) + int(n.der is not None)
            self.canvas.create_text(x, y, text=str(n.dato), font=("Arial", 12, "bold"))
            self.canvas.create_text(x, y + 30, text=f"G={grado}", font=("Arial", 9))

        _dibujar(self.arbol.raiz, 475, 50, 200)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArbolApp(root)
    root.mainloop()
