import ast

def detect_multiple_line_log(node):
    if isinstance(node, ast.ExceptHandler):
        log_count = sum(1 for n in node.body if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and getattr(n.value.func, "id", "") in ["print"])
        return log_count > 1
    return False