def add_two_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Sum:", add_two_numbers(x, y))
    except ValueError:
        print("Please enter valid numeric values.")
