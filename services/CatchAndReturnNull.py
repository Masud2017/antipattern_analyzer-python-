import ast

def detect_catch_and_return_none(node):
    return isinstance(node, ast.ExceptHandler) and any(isinstance(n, ast.Return) and isinstance(n.value, ast.Constant) and n.value.value is None for n in node.body)
