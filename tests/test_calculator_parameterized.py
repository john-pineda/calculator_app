import pytest
from calculator.calculator import Calculator

@pytest.mark.parametrize("operand1, operand2, operation, expected_result", [
    (2, 3, 'add', 5),
    (5, 2, 'subtract', 3),
    (4, 2, 'multiply', 8),
    (6, 3, 'divide', 2),
])
def test_calculator_operations(operand1, operand2, operation, expected_result):
    calculator = Calculator(operation, operand1, operand2)
    assert calculator.get_result() == expected_result
