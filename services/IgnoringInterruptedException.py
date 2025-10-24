import ast


def detect_ignoring_interrupted_exception(node):
    if isinstance(node, ast.ExceptHandler):
        if isinstance(node.type, ast.Name) and node.type.id == "KeyboardInterrupt":
            if all(isinstance(n, ast.Pass) for n in node.body):
                return True
    return False