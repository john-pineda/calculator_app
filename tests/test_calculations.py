from calculator.calculations import Calculations, Calculation
import pytest
from calculator.operations import add, subtract 

@pytest.fixture
def setup_calculations():
    Calculations.clear_history()

def test_add_calculation(setup_calculations):
    calc = Calculation(2, 2, add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_latest(setup_calculations):
    assert Calculations.get_latest() is None, "Expected None for the latest calculation with empty history"

def test_find_by_operation(setup_calculations):
    calc_add = Calculation(1, 2, add)
    calc_subtract = Calculation(3, 1, subtract)
    Calculations.add_calculation(calc_add)
    Calculations.add_calculation(calc_subtract)

    add_operations = Calculations.find_by_operation(add)
    assert add_operations == [calc_add], "Failed to find calculations by operation type"


def test_get_latest_with_empty_history():
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for the latest calculation with empty history"
