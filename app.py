#Equipo 5
#Integrantes:
#Edwin Ulises Diaz Sanchez
#Jose Raul Becerra Barcelo
#Diego Felipe Ferrer Chacon

from parsers.infix_to_postfix import InfixToPostfixParser
from builders.postfix_tree_builder import PostfixExpressionTreeBuilder
from traversals.inorder_traversal import InorderTreeTraversal
from visualizers.tkinter_visualizer import TkinterTreeVisualizer

class ExpressionTreeApp:
    """Aplicación principal para procesar árboles de expresiones."""
    def __init__(self):
        self.parser = InfixToPostfixParser()
        self.tree_builder = PostfixExpressionTreeBuilder()
        self.traversal = InorderTreeTraversal()
        self.visualizer = TkinterTreeVisualizer()
    
    def run(self):
        """Ejecuta la aplicación principal."""
        try:
            # Solicitar expresión al usuario
            expression = input("Ingrese una expresión matemática en notación infija: ")
            
            # Convertir a postfija
            postfix_expression = self.parser.parse(expression)
            print(f"Expresión en notación postfija: {postfix_expression}")
            
            # Construir el árbol
            root = self.tree_builder.build(postfix_expression)
            
            # Mostrar y visualizar el árbol
            if root:
                print("Expresión en notación infija reconstruida:")
                self.traversal.display(root)
                print("\nDibujando el árbol binario...")
                self.visualizer.visualize(root)
            else:
                print("Error al construir el árbol binario. Verifique la expresión ingresada.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    app = ExpressionTreeApp()
    app.run() 