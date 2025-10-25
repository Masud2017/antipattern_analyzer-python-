def example():
    try:
        risky_operation()
    except Exception as e:
        print("Error:", e)
        raise