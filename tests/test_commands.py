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

