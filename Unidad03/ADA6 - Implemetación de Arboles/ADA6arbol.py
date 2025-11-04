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
        nodo = self.raiz
        while nodo:
            if dato == nodo.dato:
                return True
            elif dato < nodo.dato:
                nodo = nodo.izq
            else:
                nodo = nodo.der
        return False

    # [3] Eliminar
    def eliminar(self, dato):
        def _minimo(n):
            while n.izq:
                n = n.izq
            return n

        def _eliminar(nodo, dato):
            if not nodo:
                return nodo
            if dato < nodo.dato:
                nodo.izq = _eliminar(nodo.izq, dato)
            elif dato > nodo.dato:
                nodo.der = _eliminar(nodo.der, dato)
            else:
                if nodo.izq is None:
                    return nodo.der
                elif nodo.der is None:
                    return nodo.izq
                temp = _minimo(nodo.der)
                nodo.dato = temp.dato
                nodo.der = _eliminar(nodo.der, temp.dato)
            return nodo
        self.raiz = _eliminar(self.raiz, dato)

    # [4] Recorridos
    def preOrden(self):
        resultado = []
        def _pre(n):
            if n:
                resultado.append(n.dato)
                _pre(n.izq)
                _pre(n.der)
        _pre(self.raiz)
        return resultado

    def inOrden(self):
        resultado = []
        def _in(n):
            if n:
                _in(n.izq)
                resultado.append(n.dato)
                _in(n.der)
        _in(self.raiz)
        return resultado

    def postOrden(self):
        resultado = []
        def _post(n):
            if n:
                _post(n.izq)
                _post(n.der)
                resultado.append(n.dato)
        _post(self.raiz)
        return resultado

    # [5] Altura
    def altura(self):
        def _altura(n):
            if n is None:
                return 0
            return 1 + max(_altura(n.izq), _altura(n.der))
        return _altura(self.raiz)

    # [6] Contar hojas
    def contarHojas(self):
        def _hojas(n):
            if n is None:
                return 0
            if n.izq is None and n.der is None:
                return 1
            return _hojas(n.izq) + _hojas(n.der)
        return _hojas(self.raiz)

    # [7] Contar nodos
    def contarNodos(self):
        def _nodos(n):
            if n is None:
                return 0
            return 1 + _nodos(n.izq) + _nodos(n.der)
        return _nodos(self.raiz)

    # [8] Árbol completo
    def esCompleto(self):
        if self.raiz is None:
            return True
        cola = deque([self.raiz])
        encontrado_vacio = False
        while cola:
            nodo = cola.popleft()
            if nodo:
                if encontrado_vacio:
                    return False
                cola.append(nodo.izq)
                cola.append(nodo.der)
            else:
                encontrado_vacio = True
        return True

    # [9] Árbol lleno
    def esLleno(self):
        def _lleno(n):
            if n is None:
                return True
            if (n.izq is None) != (n.der is None):
                return False
            return _lleno(n.izq) and _lleno(n.der)
        return _lleno(self.raiz)

    # [10] Eliminar árbol completo
    def eliminarArbol(self):
        self.raiz = None


# ------------------------------------------------------------
# CLASE INTERFAZ GRÁFICA
# ------------------------------------------------------------
class ArbolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Árbol Binario de Búsqueda (ABB)")
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

        tk.Button(frame, text="PreOrden", command=self.preorden, font=("Arial", 11)).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(frame, text="InOrden", command=self.inorden, font=("Arial", 11)).grid(row=1, column=3, padx=5, pady=5)
        tk.Button(frame, text="PostOrden", command=self.postorden, font=("Arial", 11)).grid(row=1, column=4, padx=5, pady=5)
        tk.Button(frame, text="Altura", command=self.altura, font=("Arial", 11)).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(frame, text="Hojas", command=self.hojas, font=("Arial", 11)).grid(row=2, column=3, padx=5, pady=5)
        tk.Button(frame, text="Nodos", command=self.nodos, font=("Arial", 11)).grid(row=2, column=4, padx=5, pady=5)
        tk.Button(frame, text="¿Completo?", command=self.completo, bg="#fff59d", font=("Arial", 11)).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(frame, text="¿Lleno?", command=self.lleno, bg="#ce93d8", font=("Arial", 11)).grid(row=3, column=3, padx=5, pady=5)

        self.canvas = tk.Canvas(self.root, bg="white", width=950, height=500)
        self.canvas.pack(pady=10)

    # -----------------------------
    # FUNCIONES DE INTERFAZ
    # -----------------------------
    def insertar(self):
        try:
            valor = int(self.entry.get())
            self.entry.delete(0, tk.END)
            self.arbol.insertar(valor)
            self.dibujar_arbol()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def buscar(self):
        try:
            valor = int(self.entry.get())
            self.entry.delete(0, tk.END)
            if self.arbol.buscar(valor):
                messagebox.showinfo("Resultado", f"El valor {valor} SÍ está en el árbol.")
            else:
                messagebox.showwarning("Resultado", f"El valor {valor} NO se encuentra.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def eliminar(self):
        try:
            valor = int(self.entry.get())
            self.entry.delete(0, tk.END)
            self.arbol.eliminar(valor)
            self.dibujar_arbol()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def limpiar(self):
        self.arbol.eliminarArbol()
        self.canvas.delete("all")

    def preorden(self):
        recorrido = self.arbol.preOrden()
        messagebox.showinfo("PreOrden", f"Recorrido: {recorrido}")

    def inorden(self):
        recorrido = self.arbol.inOrden()
        messagebox.showinfo("InOrden", f"Recorrido: {recorrido}")

    def postorden(self):
        recorrido = self.arbol.postOrden()
        messagebox.showinfo("PostOrden", f"Recorrido: {recorrido}")

    def altura(self):
        h = self.arbol.altura()
        messagebox.showinfo("Altura", f"Altura del árbol: {h}")

    def hojas(self):
        c = self.arbol.contarHojas()
        messagebox.showinfo("Hojas", f"Cantidad de hojas: {c}")

    def nodos(self):
        c = self.arbol.contarNodos()
        messagebox.showinfo("Nodos", f"Cantidad total de nodos: {c}")

    def completo(self):
        es = self.arbol.esCompleto()
        messagebox.showinfo("Árbol Completo", "✅ Es un árbol completo" if es else "❌ No es un árbol completo")

    def lleno(self):
        es = self.arbol.esLleno()
        messagebox.showinfo("Árbol Lleno", "✅ Es un árbol lleno" if es else "❌ No es un árbol lleno")

    # -----------------------------
    # DIBUJAR ÁRBOL
    # -----------------------------
    def dibujar_arbol(self):
        self.canvas.delete("all")
        if not self.arbol.raiz:
            return

        def _dibujar(nodo, x, y, dx):
            if nodo is None:
                return
            r = 20
            if nodo.izq:
                self.canvas.create_line(x, y, x - dx, y + 80, width=2)
                _dibujar(nodo.izq, x - dx, y + 80, dx / 1.8)
            if nodo.der:
                self.canvas.create_line(x, y, x + dx, y + 80, width=2)
                _dibujar(nodo.der, x + dx, y + 80, dx / 1.8)
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#64b5f6", outline="black", width=2)
            self.canvas.create_text(x, y, text=str(nodo.dato), font=("Arial", 12, "bold"))

        _dibujar(self.arbol.raiz, 475, 50, 200)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArbolApp(root)
    root.mainloop()
