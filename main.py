import tkinter as tk

from tkinter import messagebox


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node  # Duplicado, no hace nada

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)

        # Caso Izquierda-Izquierda
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Caso Derecha-Derecha
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Caso Izquierda-Derecha
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Caso Derecha-Izquierda
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)  # CORREGIDO AQUÍ

        return node


class AVLVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador AVL - Ingeniería Informática")
        self.tree = AVLTree()
        self.tree_root = None

        # Controles
        self.control_frame = tk.Frame(root, pady=10)
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(self.control_frame, text="Valor:").pack(side=tk.LEFT, padx=5)
        self.entry = tk.Entry(self.control_frame, width=10)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind("<Return>", lambda e: self.handle_insert())

        self.btn_insert = tk.Button(
            self.control_frame, text="Insertar",
            command=self.handle_insert, bg="#4CAF50", fg="white")
        self.btn_insert.pack(side=tk.LEFT, padx=5)

        self.btn_clear = tk.Button(
            self.control_frame, text="Limpiar", command=self.clear_canvas)
        self.btn_clear.pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(root, width=1000, height=600, bg="#F0F0F0")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def handle_insert(self):
        try:
            val = int(self.entry.get())
            self.tree_root = self.tree.insert(self.tree_root, val)
            self.entry.delete(0, tk.END)
            self.refresh_view()
        except ValueError:
            messagebox.showwarning("Error", "Ingresa un número entero válido")

    def refresh_view(self):
        self.canvas.delete("all")
        if self.tree_root:
            # Empezamos el dibujo (x=centro, y=50, offset=250)
            self.draw_node_recursive(self.tree_root, 500, 50, 250)

    def draw_node_recursive(self, node, x, y, x_offset):
        if not node:
            return

        radius = 20
        v_spacing = 70

        # Dibujar líneas
        if node.left:
            self.canvas.create_line(
                x, y, x - x_offset, y + v_spacing, width=2, fill="#757575")
            self.draw_node_recursive(
                node.left, x - x_offset, y + v_spacing, x_offset / 2)
        if node.right:
            self.canvas.create_line(
                x, y, x + x_offset, y + v_spacing, width=2, fill="#757575")
            self.draw_node_recursive(
                node.right, x + x_offset, y + v_spacing, x_offset / 2)

        # Dibujar Círculo
        self.canvas.create_oval(x-radius, y-radius, x+radius,
                                y+radius, fill="#a1c4fd",
                                outline="#2196F3", width=2)
        # Dibujar Texto
        self.canvas.create_text(x, y, text=str(
            node.key), font=("Arial", 10, "bold"))
        # Mostrar altura y balance para la materia
        self.canvas.create_text(x, y - 35,
                                text=f"h={node.height} | b={
                                    self.tree.get_balance(node)}",
                                fill="#555", font=("Arial", 8))

    def clear_canvas(self):
        self.tree_root = None
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = AVLVisualizer(root)
    root.mainloop()
