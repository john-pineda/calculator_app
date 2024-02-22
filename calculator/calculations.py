class Calculations:
    _calculation_history = []

    @classmethod
    def add_calculation(cls, calculation):
        cls._calculation_history.append(calculation)

    @classmethod
    def get_history(cls):
        return cls._calculation_history

    # Other methods for managing calculations...
