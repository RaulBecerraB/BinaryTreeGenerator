#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Equipo 5
#Integrantes:
#Edwin Ulises Diaz Sanchez
#Jose Raul Becerra Barcelo
#Diego Felipe Ferrer Chacon

from abc import ABC, abstractmethod

class IExpressionParser(ABC):
    """Interfaz para los analizadores de expresiones."""
    @abstractmethod
    def parse(self, expression):
        """Analiza una expresión y la convierte a otro formato."""
        pass

class IExpressionTreeBuilder(ABC):
    """Interfaz para los constructores de árboles de expresiones."""
    @abstractmethod
    def build(self, expression):
        """Construye un árbol a partir de una expresión."""
        pass

class ITreeTraversal(ABC):
    """Interfaz para las estrategias de recorrido de árboles."""
    @abstractmethod
    def traverse(self, node):
        """Recorre un árbol y realiza una operación en cada nodo."""
        pass

class ITreeVisualizer(ABC):
    """Interfaz para los visualizadores de árboles."""
    @abstractmethod
    def visualize(self, root):
        """Visualiza un árbol."""
        pass 