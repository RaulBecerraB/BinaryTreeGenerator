#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Equipo 5
#Integrantes:
#Edwin Ulises Diaz Sanchez
#Jose Raul Becerra Barcelo
#Diego Felipe Ferrer Chacon

from interfaces.interfaces import ITreeTraversal
from utils.operator_utils import OperatorUtils

class InorderTreeTraversal(ITreeTraversal):
    """Implementa el recorrido inorden para un árbol binario."""
    def __init__(self):
        self.result = []
    
    def traverse(self, node):
        """Recorre el árbol en inorden y guarda el resultado."""
        if node is None:
            return
        
        if OperatorUtils.is_operator(node.value):
            self.result.append("(")
        
        self.traverse(node.left)
        self.result.append(node.value)
        self.traverse(node.right)
        
        if OperatorUtils.is_operator(node.value):
            self.result.append(")")
        
        return ' '.join(self.result)
    
    def display(self, node):
        """Muestra el recorrido inorden por pantalla."""
        self.result = []
        if node is not None:
            if OperatorUtils.is_operator(node.value):
                print("(", end="")
            self.display(node.left)
            print(node.value, end=" ")
            self.display(node.right)
            if OperatorUtils.is_operator(node.value):
                print(")", end="") 