"""Simple calculator module used for the Git branching and merge-conflict demo."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def power(a, b):
    return a ** b


def divide(a, b):
    if b == 0:
        print("Warning: division by zero, returning None")
        return None
    return a / b


def describe():
    """Return a one-line description of this module."""
    return "Calculator v1.1 - basic arithmetic with safe division"


if __name__ == "__main__":
    print(describe())
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", subtract(7, 4))
    print("2 ^ 5 =", power(2, 5))
    print("8 / 2 =", divide(8, 2))
