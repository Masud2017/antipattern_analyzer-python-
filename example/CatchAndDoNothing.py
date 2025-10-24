def divide_numbers():
    try:
        a = 10 / 0
    except ZeroDivisionError:
        pass

    try:
        b = 20 / 0
    except ZeroDivisionError:
        pass

    try:
        c = 30 / 0
    except ZeroDivisionError:
        pass

    try:
        d = 40 / 0
    except ZeroDivisionError:
        pass

    try:
        e = 50 / 0
    except ZeroDivisionError:
        pass

    try:
        f = 60 / 0
    except ZeroDivisionError:
        pass

    try:
        g = 70 / 0
    except ZeroDivisionError:
        pass

    return None

def compute_values():
    for i in range(5):
        try:
            value = i / (i - 3)
        except ZeroDivisionError:
            pass
