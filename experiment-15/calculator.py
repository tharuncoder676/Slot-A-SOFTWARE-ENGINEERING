"""Simple calculator module used for the Git branching and merge-conflict demo."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def describe():
    """Return a one-line description of this module."""
    return "Calculator v2.0 - arithmetic operations with multiply support"


if __name__ == "__main__":
    print(describe())
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", subtract(7, 4))
    print("6 * 5 =", multiply(6, 5))
    print("8 / 2 =", divide(8, 2))
