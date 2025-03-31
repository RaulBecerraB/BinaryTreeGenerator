# Binary Expression Tree Generator

An application that generates binary trees from mathematical expressions, following SOLID principles.

## Team 5
- Edwin Ulises Diaz Sanchez
- Jose Raul Becerra Barcelo
- Diego Felipe Ferrer Chacon

## Project Structure

The project is organized into the following modules:

```
BinaryTreeGenerator/
├── app.py                       # Application entry point
├── models/                      # Data models
│   ├── __init__.py
│   └── node.py                  # Tree node definition
├── interfaces/                  # Abstract interfaces
│   ├── __init__.py
│   └── interfaces.py            # Interface definitions
├── utils/                       # Utilities
│   ├── __init__.py
│   ├── operator_utils.py        # Operator utilities
│   └── expression_tokenizer.py  # Expression tokenizer
├── parsers/                     # Expression parsers
│   ├── __init__.py
│   └── infix_to_postfix.py      # Infix to postfix conversion
├── builders/                    # Tree builders
│   ├── __init__.py
│   └── postfix_tree_builder.py  # Builder from postfix notation
├── traversals/                  # Tree traversals
│   ├── __init__.py
│   └── inorder_traversal.py     # Inorder traversal
└── visualizers/                 # Tree visualizers
    ├── __init__.py
    └── tkinter_visualizer.py    # Tkinter visualizer
```

## Execution

To run the application:

```bash
python app.py
```

## Applied SOLID Principles

1. **S** - Single Responsibility: Each class has a single responsibility
2. **O** - Open/Closed: The code is open for extension, closed for modification
3. **L** - Liskov Substitution: Implementations can substitute their interfaces
4. **I** - Interface Segregation: Specific interfaces are used instead of general ones
5. **D** - Dependency Inversion: The code depends on abstractions, not concrete implementations 