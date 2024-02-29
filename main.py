from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.hello import HelloCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.exit import ExitCommand

def get_user_input():
    return input(">>> ")

def get_numbers_from_user():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    return a, b

if __name__ == "__main__":
    print("Welcome to the Interactive Calculator!")

    while True:
        print("Available commands: add, subtract, multiply, divide, hello, goodbye, exit")
        user_input = get_user_input()

        if user_input.lower() == "exit":
            exit_command = ExitCommand()
            exit_command.execute()
        elif user_input.lower() == "hello":
            greet_command = HelloCommand()
            greet_command.execute()
        elif user_input.lower() == "goodbye":
            goodbye_command = GoodbyeCommand()
            goodbye_command.execute()
        elif user_input.lower() in ["add", "subtract", "multiply", "divide"]:
            numbers = get_numbers_from_user()
            
            if user_input.lower() == "add":
                add_command = AddCommand()
                add_command.execute(*numbers)
            elif user_input.lower() == "subtract":
                subtract_command = SubtractCommand()
                subtract_command.execute(*numbers)
            elif user_input.lower() == "multiply":
                multiply_command = MultiplyCommand()
                multiply_command.execute(*numbers)
            elif user_input.lower() == "divide":
                divide_command = DivideCommand()
                divide_command.execute(*numbers)
        else:
            print("Invalid command. Please try again.")
