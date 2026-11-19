def add(a, b):
    if b is None:
        return a

    return a + b


def record(value, history=None):
    if history is None:
        history = []

    history.append(value)
    return history


def broken_total():
    return missing_total
