import ast
def detect_log_and_throw(node):
    if isinstance(node, ast.ExceptHandler):
        has_log = any(isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and getattr(n.value.func, "id", "") in ["print"] for n in node.body)
        has_raise = any(isinstance(n, ast.Raise) for n in node.body)
        return has_log and has_raise
    return False