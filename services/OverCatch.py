import ast 


def detect_over_catch(node):
    if isinstance(node, ast.ExceptHandler) and node.type is not None and isinstance(node.type, ast.Tuple):
        return True
    return False