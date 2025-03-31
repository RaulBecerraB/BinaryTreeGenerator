#Equipo 5
#Integrantes:
#Edwin Ulises Diaz Sanchez
#Jose Raul Becerra Barcelo
#Diego Felipe Ferrer Chacon

import tkinter as tk
from interfaces.interfaces import ITreeVisualizer

class TkinterTreeVisualizer(ITreeVisualizer):
    """Visualiza un árbol binario usando Tkinter."""
    def visualize(self, root):
        """Crea una visualización gráfica del árbol."""
        window = tk.Tk()
        window.title("Árbol Binario de Expresión")
        
        # Configuraciones para que la ventana aparezca al frente
        window.attributes('-topmost', True)  # Mantiene la ventana sobre otras
        window.update()  # Actualiza la ventana
        window.focus_force()  # Fuerza el enfoque en esta ventana
        
        canvas = tk.Canvas(window, width=500, height=400, bg="white")
        canvas.pack()
        
        self._draw_node(canvas, root, 250, 50, 100)
        
        # Quita el atributo topmost después de mostrar para permitir interacción normal
        window.after(1000, lambda: window.attributes('-topmost', False))
        
        window.mainloop()
    
    def _draw_node(self, canvas, node, x, y, dx):
        """Dibuja un nodo y sus conexiones en el canvas."""
        if node is None:
            return
            
        r = 20
        canvas.create_oval(x - r, y - r, x + r, y + r, fill="lightblue")
        canvas.create_text(x, y, text=node.value, font=("Arial", 12, "bold"))
        
        if node.left:
            canvas.create_line(x, y + r, x - dx, y + 60 - r, arrow=tk.LAST)
            self._draw_node(canvas, node.left, x - dx, y + 60, dx // 2)
            
        if node.right:
            canvas.create_line(x, y + r, x + dx, y + 60 - r, arrow=tk.LAST)
            self._draw_node(canvas, node.right, x + dx, y + 60, dx // 2) 