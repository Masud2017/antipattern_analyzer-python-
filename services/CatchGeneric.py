import ast

def detect_catch_generic(node):
    return isinstance(node, ast.ExceptHandler) and (node.type is None or (isinstance(node.type, ast.Name) and node.type.id == "Exception"))