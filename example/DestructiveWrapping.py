def example():
    try:
        risky_operation()
    except ValueError as e:
        raise RuntimeError("Something went wrong")  # loses original context