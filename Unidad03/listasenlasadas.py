import tkinter as tk
from tkinter import messagebox
import ast
import random
import sys

# ----------------------------------------------
# Clase de ejemplo
# ----------------------------------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"


# ----------------------------------------------
# Nodo
# ----------------------------------------------
class Node:
    def __init__(self, data, address=None):
        self.data = data
        self.next = None
        # Si el usuario elige una dirección, usarla. Si no, generar una aleatoria.
        self.address = address or hex(random.randint(0x1000, 0xFFFF))
        self.memory = self.get_memory_size()
    def get_memory_size(self):
        return sys.getsizeof(self) + sys.getsizeof(self.data)


# ----------------------------------------------
# Lista enlazada
# ----------------------------------------------
class LinkedList:
    def __init__(self, canvas, memory_label):
        self.head = None
        self.canvas = canvas
        self.memory_label = memory_label
        self.count = 0
        self.used_addresses = set()

    def address_exists(self, addr):
        return addr in self.used_addresses

    def insert(self, data, custom_address=None):
        # Si el usuario elige una dirección específica
        if custom_address:
            addr = custom_address.lower()
            if not addr.startswith("0x"):
                messagebox.showwarning("Error", "Las direcciones deben comenzar con '0x'.")
                return
            if self.address_exists(addr):
                messagebox.showerror("Error", f"La dirección {addr} ya está ocupada.")
                return
            new_node = Node(data, address=addr)
        else:
            new_node = Node(data)
            # Evitar duplicados aleatorios
            while new_node.address in self.used_addresses:
                new_node.address = hex(random.randint(0x1000, 0xFFFF))

        self.used_addresses.add(new_node.address)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1
        self.draw()
        self.update_memory_label()
        messagebox.showinfo(
            "Insertar",
            f"Elemento '{data}' insertado.\nDirección: {new_node.address}\nMemoria ocupada: {new_node.memory} bytes"
        )

    def delete(self, query):
        if not self.head:
            messagebox.showwarning("Eliminar", "La lista está vacía.")
            return

        mode = "valor"
        if query.startswith("0x"):
            mode = "direccion"
        elif query.lower().startswith("nodo "):
            mode = "nodo"

        current = self.head
        previous = None
        index = 0

        while current:
            match = (
                (mode == "valor" and str(current.data) == query)
                or (mode == "direccion" and current.address.lower() == query.lower())
                or (mode == "nodo" and f"nodo {index}" == query.lower())
            )
            if match:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                self.used_addresses.remove(current.address)
                messagebox.showinfo(
                    "Eliminar",
                    f"Nodo {index} eliminado.\n"
                    f"Dirección liberada: {current.address}\n"
                    f"Memoria liberada: {current.memory} bytes"
                )
                self.count -= 1
                self.draw()
                self.update_memory_label()
                return
            previous = current
            current = current.next
            index += 1

        messagebox.showwarning("No encontrado", f"No se encontró ningún nodo con '{query}'.")

    def total_memory(self):
        total = 0
        current = self.head
        while current:
            total += current.memory
            current = current.next
        return total

    def update_memory_label(self):
        total = self.total_memory()
        self.memory_label.config(
            text=f"🔹 Memoria total usada: {total} bytes ({round(total/1024,2)} KB)"
        )

    def draw(self, highlight_index=None):
        self.canvas.delete("all")
        current = self.head
        x, y = 70, 150
        node_width, node_height, arrow_length = 340, 140, 90
        index = 0

        while current:
            tipo = type(current.data).__name__
            valor = str(current.data)
            if len(valor) > 25:
                valor = valor[:25] + "..."
            next_addr = current.next.address if current.next else "None"

            node_text = (
                f"Nodo {index}\n"
                f"Valor: {valor}\n"
                f"Tipo: {tipo}\n"
                f"Dir: {current.address}\n"
                f"Apunta a: {next_addr}\n"
                f"Mem: {current.memory} bytes"
            )

            color = "#00b8d9" if index == highlight_index else "#007acc"
            outline = "#ffffff" if index == highlight_index else "#00ffff"
            self._draw_node_box(x, y, node_width, node_height, node_text, color, outline)

            if current.next:
                self.canvas.create_line(
                    x + node_width, y + node_height / 2,
                    x + node_width + arrow_length, y + node_height / 2,
                    arrow=tk.LAST, width=3, fill="#00ffff"
                )

            current = current.next
            x += node_width + arrow_length
            index += 1

    def _draw_node_box(self, x, y, w, h, text, color, outline):
        radius = 20
        self.canvas.create_rectangle(x+3, y+3, x+w+3, y+h+3, fill="#0a0a0a", outline="")
        self.canvas.create_rectangle(x + radius, y, x + w - radius, y + h, fill=color, outline=outline, width=2)
        self.canvas.create_rectangle(x, y + radius, x + w, y + h - radius, fill=color, outline=outline, width=2)
        for dx, dy in [(0, 0), (w - 2 * radius, 0), (0, h - 2 * radius), (w - 2 * radius, h - 2 * radius)]:
            self.canvas.create_oval(x + dx, y + dy, x + dx + 2 * radius, y + dy + 2 * radius,
                                    fill=color, outline=outline, width=2)
        self.canvas.create_text(x + w / 2, y + h / 2, text=text, fill="white",
                                font=("Consolas", 11, "bold"), justify="center")


# ----------------------------------------------
# Interfaz gráfica
# ----------------------------------------------
class LinkedListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista enlazada - Inserción por dirección de memoria")
        self.root.geometry("1420x780")
        self.root.config(bg="#0d1117")

        self.canvas = tk.Canvas(root, bg="#161b22", height=420, highlightthickness=0)
        self.canvas.pack(pady=30, fill="x")

        self.memory_label = tk.Label(root, text="🔹 Memoria total usada: 0 bytes",
                                     bg="#0d1117", fg="#00ffff", font=("Segoe UI", 12, "bold"))
        self.memory_label.pack(pady=(0, 10))

        self.linked_list = LinkedList(self.canvas, self.memory_label)

        frame = tk.Frame(root, bg="#0d1117")
        frame.pack(pady=10)

        tk.Label(frame, text="Valor:", bg="#0d1117", fg="white", font=("Segoe UI", 12)).grid(row=0, column=0, padx=5)
        self.entry_value = tk.Entry(frame, font=("Segoe UI", 12), width=30)
        self.entry_value.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Dirección (opcional):", bg="#0d1117", fg="white", font=("Segoe UI", 12)).grid(row=0, column=2, padx=5)
        self.entry_address = tk.Entry(frame, font=("Segoe UI", 12), width=15)
        self.entry_address.grid(row=0, column=3, padx=5)

        tk.Button(frame, text="Insertar", command=self.insert, bg="#238636", fg="white", width=12, height=1).grid(row=0, column=4, padx=8)
        tk.Button(frame, text="Eliminar", command=self.delete, bg="#da3633", fg="white", width=12, height=1).grid(row=0, column=5, padx=8)
        tk.Button(frame, text="Buscar", command=self.search, bg="#f0a30a", fg="black", width=12, height=1).grid(row=0, column=6, padx=8)

        tk.Label(root,
                 text="💡 Puedes escribir una dirección manual (ej. 0xABCD) o dejar vacío para que se asigne automáticamente.",
                 bg="#0d1117", fg="#cccccc", font=("Segoe UI", 11)).pack(pady=10)

    def parse_input(self, text):
        try:
            return ast.literal_eval(text)
        except Exception:
            try:
                env = {"Persona": Persona}
                return eval(text, env)
            except Exception:
                return text

    def insert(self):
        value = self.entry_value.get().strip()
        addr = self.entry_address.get().strip() or None
        if not value:
            messagebox.showwarning("Error", "Ingresa un valor para insertar.")
            return
        data = self.parse_input(value)
        self.linked_list.insert(data, custom_address=addr)
        self.entry_value.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

    def delete(self):
        query = self.entry_value.get().strip()
        if not query:
            messagebox.showwarning("Error", "Ingresa el valor, dirección o nodo a eliminar.")
            return
        self.linked_list.delete(query)
        self.entry_value.delete(0, tk.END)

    def search(self):
        query = self.entry_value.get().strip()
        if not query:
            messagebox.showwarning("Error", "Ingresa el valor, dirección o nodo a buscar.")
            return
        self.linked_list.search(query)


# ----------------------------------------------
# Ejecutar programa
# ----------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListApp(root)
    root.mainloop()

