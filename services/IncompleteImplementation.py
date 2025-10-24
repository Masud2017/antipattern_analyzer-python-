import ast

def detect_incomplete_implementation(node):
    if isinstance(node, ast.ExceptHandler):
        for n in node.body:
            if isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and ("TODO" in str(n.value.value) or "NotImplemented" in str(n.value.value)):
                return True
    return False