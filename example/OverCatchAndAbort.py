import sys
def example():
    try:
        risky_operation()
    except (ValueError, TypeError, Exception):
        sys.exit(1)