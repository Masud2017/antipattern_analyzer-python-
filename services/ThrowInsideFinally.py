import ast 

def detect_throw_inside_finally(node):
    if isinstance(node, ast.Try):
        for n in node.finalbody:
            if isinstance(n, ast.Raise):
                return True
    return False