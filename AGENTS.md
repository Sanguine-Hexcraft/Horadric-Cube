# Agent Instructions for Horadric-Cube

## Project Overview
Horadric Cube is a static site generator built with Python. It handles markdown/text parsing into HTML nodes using a tree of node classes (HTMLNode, LeafNode, ParentNode, TextNode).

## Build & Test Commands

### Running Tests
```bash
# Run all tests
python3 -m unittest discover -s src

# Run all tests with verbose output
python3 -m unittest discover -vv src

# Run a specific test file
python3 -m unittest src.test_textnode

# Run a specific test class
python3 -m unittest src.test_textnode.TestTextNode

# Run a specific test method
python3 -m unittest src.test_textnode.TestTextNode.test_eq
```

### Running the Application
```bash
# Execute main entry point
python3 src/main.py

# Or use the convenience script
./main.sh
```

### Python Execution
```bash
# Run any module directly
python3 -m src.main
```

## Code Style Guidelines

### Python Version
- Target Python 3.12+

### Imports
- Use absolute imports from the package: `from textnode import TextNode` (not `from .textnode`)
- Order: standard library first, then third-party, then local
- No import grouping with blank lines in this codebase

### Naming Conventions
- **Classes**: PascalCase (e.g., `TextNode`, `HTMLNode`, `LeafNode`)
- **Functions/methods**: snake_case (e.g., `text_node_to_html_node`, `split_nodes_delimiter`)
- **Variables**: snake_case (e.g., `text_type`, `new_nodes`, `children_string`)
- **Enum values**: UPPER_SNAKE_CASE strings (e.g., `TextType.BOLD.value` returns `"bold"`)
- **Constants**: UPPER_SNAKE_CASE

### Type Annotations
- No type hints currently used in the codebase
- When adding new code, consider adding type hints for better IDE support and documentation

### Docstrings & Comments
- Inline comments are used sparingly
- No docstrings currently present
- If adding docstrings, use Google-style or NumPy-style

### Error Handling
- Raise `ValueError` for invalid input/state (see `LeafNode.to_html()`)
- Raise `Exception` for general errors (see `split_nodes_delimiter`)
- Use descriptive error messages

### String Formatting
- Use f-strings: `f"TextNode({self.text}, {self.text_type.value}, {self.url})"`
- Use single quotes for strings unless double quotes are needed

### Class Structure
```
class ClassName:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        pass
```
- Two blank lines between top-level classes/functions
- One blank line between methods

### Node Class Hierarchy
```
HTMLNode (base class)
├── LeafNode (no children, has value)
└── ParentNode (has children list)
```

### Testing Conventions
- Use `unittest.TestCase`
- Test files named `test_<module>.py` in `src/` directory
- Test classes named `Test<ClassName>`
- Test methods named `test_<description>`
- Use `self.assertEqual()`, `self.assertRaises()`, `self.assertNotEqual()`
- Include `if __name__ == "__main__": unittest.main()` at the end

### Common Patterns

#### Equality Comparison
```python
def __eq__(self, other):
    return (
        self.attr1 == other.attr1
        and self.attr2 == other.attr2
    )
```

#### String Building
```python
result = ""
for item in items:
    result += f"prefix_{item}_suffix"
return result
```

#### Node Conversion (if/elif chain)
```python
def convert(self, node):
    if node.type == Type.A:
        return something
    if node.type == Type.B:
        return other
    raise ValueError("Unknown type")
```

### File Organization
```
src/
    main.py           # Entry point with main() function
    htmlnode.py       # HTML node classes (HTMLNode, LeafNode, ParentNode)
    textnode.py       # Text node classes (TextNode, TextType enum)
    nodes_delimiter.py # Functions for splitting nodes by delimiters
    test_*.py         # Test files

public/              # Static site output
main.sh             # Build script
test.sh             # Test script
```

## Linting & Type Checking
- No linting or type checking tools are currently configured
- Run tests to verify correctness
- Follow existing code style when making changes

## Git Workflow
- Commit messages should be concise (1-2 sentences)
- Focus on the "why" not the "what"
