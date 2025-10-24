import ast
import os
from dotenv import load_dotenv
load_dotenv()

def detect_catch_and_do_nothing(node):
    return isinstance(node, ast.ExceptHandler) and (len(node.body) == 0 or all(isinstance(n, ast.Pass) for n in node.body))