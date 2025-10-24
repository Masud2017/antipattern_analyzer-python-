import ast 

def detect_over_catch_and_abort(node):
    if isinstance(node, ast.ExceptHandler):
        for n in node.body:
            if isinstance(n, ast.Call) and getattr(n.func, "id", "") in ["exit", "sys.exit"]:
                return True
    return False
