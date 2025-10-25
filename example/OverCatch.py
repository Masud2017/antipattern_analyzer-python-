def example():
    try:
        risky_operation()
    except (ValueError, TypeError):
        print("Caught multiple")