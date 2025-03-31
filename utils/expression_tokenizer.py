#Equipo 5
#Integrantes:
#Edwin Ulises Diaz Sanchez
#Jose Raul Becerra Barcelo
#Diego Felipe Ferrer Chacon

import re

class ExpressionTokenizer:
    """Clase para tokenizar expresiones matemáticas."""
    @staticmethod
    def tokenize(expression):
        """Divide una expresión en tokens."""
        return re.findall(r'\d+|[+\-*/^√()]|[a-zA-Z]', expression) 