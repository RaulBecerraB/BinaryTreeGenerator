from interfaces.interfaces import IExpressionTreeBuilder

from interfaces.interfaces import IExpressionTreeBuilder
from models.node import TreeNode
from utils.operator_utils import OperatorUtils

class PostfixExpressionTreeBuilder(IExpressionTreeBuilder):
    """Construye un árbol binario a partir de una expresión postfija."""
    def build(self, expression):
        """Construye el árbol a partir de una expresión postfija."""
        stack = []
        tokens = expression.split()
        
        for token in tokens:
            if token.isalnum():
                stack.append(TreeNode(token))
            elif OperatorUtils.is_operator(token):
                if not stack:  # Validación de la pila
                    raise ValueError(f"Expresión inválida: no hay suficientes operandos para {token}")
                
                node = TreeNode(token)
                node.right = stack.pop()
                
                if token != '√':  # La raíz cuadrada solo tiene un operando (prefijo)
                    if not stack:  # Validación adicional para operadores binarios
                        raise ValueError(f"Expresión inválida: no hay suficientes operandos para {token}")
                    node.left = stack.pop()
                
                stack.append(node)
        
        if len(stack) != 1:
            raise ValueError("Expresión inválida: operadores o operandos desbalanceados")
            
        return stack[0] if stack else None 