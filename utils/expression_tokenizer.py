import re

class ExpressionTokenizer:
    """Clase para tokenizar expresiones matemáticas."""
    @staticmethod
    def tokenize(expression):
        """Divide una expresión en tokens."""
        return re.findall(r'\d+|[+\-*/^√()]|[a-zA-Z]', expression) 