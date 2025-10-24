import ast

def detect_nested_try(node):
    if isinstance(node, ast.Try):
        for n in node.body:
            if isinstance(n, ast.Try):
                return True
    return False