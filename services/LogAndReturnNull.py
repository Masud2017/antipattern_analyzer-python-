import ast

def detect_log_and_return_none(node):
    if isinstance(node, ast.ExceptHandler):
        has_log = any(isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and getattr(n.value.func, "id", "") in ["print"] for n in node.body)
        has_return_none = any(isinstance(n, ast.Return) and isinstance(n.value, ast.Constant) and n.value.value is None for n in node.body)
        return has_log and has_return_none
    return False
