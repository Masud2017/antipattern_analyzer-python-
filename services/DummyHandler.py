import ast

def detect_dummy_handler(node):
    if isinstance(node, ast.ExceptHandler):
        for n in node.body:
            if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and getattr(n.value.func, "id", "") in ["print"]:
                return True
    return False