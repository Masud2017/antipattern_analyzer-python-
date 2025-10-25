def example():
    try:
        risky_operation()
    except Exception:
        print("Oops")  # useless handler