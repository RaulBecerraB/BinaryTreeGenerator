from collections import deque

from collections import deque
from interfaces.interfaces import IExpressionParser
from utils.expression_tokenizer import ExpressionTokenizer
from utils.operator_utils import OperatorUtils

class InfixToPostfixParser(IExpressionParser):
    """Clase para convertir expresiones infijas a postfijas."""
    def __init__(self, tokenizer=None):
        self.tokenizer = tokenizer or ExpressionTokenizer()
    
    def parse(self, expression):
        """Convierte una expresión infija a postfija."""
        salida = []
        pila = deque()
        precedencia = OperatorUtils.get_precedence()
        tokens = self.tokenizer.tokenize(expression)
        
        for token in tokens:
            if token.isalnum():
                salida.append(token)
            elif token == '(':
                pila.append(token)
            elif token == ')':
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                if pila:  # Asegurarse de que hay un paréntesis de apertura para eliminar
                    pila.pop()
            else:
                while pila and precedencia.get(pila[-1], 0) >= precedencia.get(token, 0):
                    salida.append(pila.pop())
                pila.append(token)
        
        while pila:
            salida.append(pila.pop())
            
        return ' '.join(salida) 