class DivideCommand:
    def execute(self, a, b):
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = a / b
            print(f"{a} / {b} = {result}")