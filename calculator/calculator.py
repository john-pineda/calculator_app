from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return a + b

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return a - b

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return a * b

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("null")
        return a / b