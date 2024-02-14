class Calculator:
    _calculation_history = []

    @classmethod
    def get_operation_history(cls):
        return cls._calculation_history

    def __init__(self, operation, operand1, operand2, result):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self._calculation_history.append(self)

    def get_calculation(self):
        return f"{self.operand1} {self.operation} {self.operand2} = {self.result}"

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Not divisible by 0")
        return a / b

    @staticmethod
    def new_method(a, b):
        return a * b
