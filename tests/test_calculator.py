from calculator.calculator import Calculator

def test_multiplication():
    calculator = Calculator("multiply", 3, 4, 12)
    assert calculator.get_calculation() == "3 multiply 4 = 12"
    assert calculator.get_calculation() in [calc.get_calculation() for calc in Calculator.get_operation_history()]

def test_division():
    calculator = Calculator("divide", 6, 2, 3)
    assert calculator.get_calculation() == "6 divide 2 = 3"
    assert calculator.get_calculation() in [calc.get_calculation() for calc in Calculator.get_operation_history()]

def test_new_method():
    calculator = Calculator("new_method", 2, 3, 5)
    assert calculator.get_calculation() == "2 new_method 3 = 5"
    assert calculator.get_calculation() in [calc.get_calculation() for calc in Calculator.get_operation_history()]
