'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(2, 2) == 0

def test_multiplication():
    '''Test that multiplication function works '''    
    assert multiply(3, 4) == 12

def test_division():
    '''Test that division function works '''    
    assert divide(6, 2) == 3

# Additional tests for edge cases or specific scenarios:
def test_divide_by_zero():
    '''Test that division by zero raises a ZeroDivisionError'''
    # Use pytest's context manager to check for the exception
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
