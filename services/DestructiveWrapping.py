import ast

def detect_destructive_wrapping(node):
    if isinstance(node, ast.Raise):
        return node.exc is not None and not hasattr(node.exc, "cause")
    return False