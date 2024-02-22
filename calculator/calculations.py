from typing import List

class Calculation:
    def __init__(self, operand1, operand2, operation):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation):
        cls.history.append(calculation)

    @classmethod
    def get_latest(cls):
        return cls.history[-1] if cls.history else None

    @classmethod
    def find_by_operation(cls, operation_type):
        return [calc for calc in cls.history if calc.operation == operation_type]

    @classmethod
    def clear_history(cls):
        cls.history = []
