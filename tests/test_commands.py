from app.commands.exit import ExitCommand
from unittest.mock import patch
import sys
import pytest

def test_exit_command(capsys):
    with patch("sys.exit") as mock_exit:
        exit_command = ExitCommand()
        exit_command.execute()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Exiting now..."
    mock_exit.assert_called_once_with(0)


from app.commands.hello import HelloCommand
from unittest.mock import patch
import pytest

def test_greet_command(capsys):
    greet_command = HelloCommand()
    greet_command.execute()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


from app.commands.goodbye import GoodbyeCommand
from unittest.mock import patch
import pytest

def test_goodbye_command(capsys):
    goodbye_command = GoodbyeCommand()
    goodbye_command.execute()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Goodbye, World!"


# calculator_app/tests/test_commands.py
from app.commands.add import AddCommand
from unittest.mock import patch
import pytest

def test_add_command(capsys):
    add_command = AddCommand()
    add_command.execute(3, 5)

    captured = capsys.readouterr()
    assert captured.out.strip() == "3 + 5 = 8"

from app.commands.subtract import SubtractCommand
from unittest.mock import patch
import pytest

from app.commands.subtract import SubtractCommand
from unittest.mock import patch
import pytest

def test_subtract_command(capsys):
    subtract_command = SubtractCommand()
    subtract_command.execute(8, 4)

    captured = capsys.readouterr()
    assert captured.out.strip() == "8 - 4 = 4"

from app.commands.multiply import MultiplyCommand
from unittest.mock import patch
import pytest

def test_multiply_command(capsys):
    multiply_command = MultiplyCommand()
    multiply_command.execute(3, 5)

    captured = capsys.readouterr()
    assert captured.out.strip() == "3 * 5 = 15"

from app.commands.divide import DivideCommand
from unittest.mock import patch
import pytest

def test_divide_command(capsys):
    divide_command = DivideCommand()
    divide_command.execute(10, 2)

    captured = capsys.readouterr()
    assert captured.out.strip() in ["10 / 2 = 5", "10 / 2 = 5.0"]
