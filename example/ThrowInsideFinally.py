def example():
    try:
        risky_operation()
    finally:
        raise RuntimeError("Error in finally")