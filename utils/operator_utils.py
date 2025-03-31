#Equipo 5
#Integrantes:
#Edwin Ulises Diaz Sanchez
#Jose Raul Becerra Barcelo
#Diego Felipe Ferrer Chacon

class OperatorUtils:
    """Utilidades para trabajar con operadores matemáticos."""
    @staticmethod
    def is_operator(c):
        """Determina si un carácter es un operador."""
        return c in {'+', '-', '*', '/', '^', '√'}
    
    @staticmethod
    def get_precedence():
        """Devuelve un diccionario con las precedencias de los operadores."""
        return {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '√': 3, '(': 0} 