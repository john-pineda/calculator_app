from calculator.calculator import Calculator

def main():
    # Example usage of the Calculator class
    a = Decimal('5')
    b = Decimal('2')

    result_add = Calculator.add(a, b)
    print(f"The result of {a} add {b} is equal to {result_add}")

    result_subtract = Calculator.subtract(a, b)
    print(f"The result of {a} subtract {b} is equal to {result_subtract}")

    result_multiply = Calculator.multiply(a, b)
    print(f"The result of {a} multiply {b} is equal to {result_multiply}")

    try:
        result_divide = Calculator.divide(a, 0)
        print(f"The result of {a} divide 0 is equal to {result_divide}")
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
