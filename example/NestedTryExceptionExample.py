def example():
    try:
        try:
            risky_operation()
        except ValueError:
            print("Inner exception")
    except Exception:
        print("Outer exception")