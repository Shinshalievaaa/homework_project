import pytest

from src.decorators import log


@log()
def example_success_function():
    return 'success'


@log()
def example_err_function():
    # some potentially failing operation
    raise ValueError("Something went wrong!")



def test_successful_decorators(capsys):
    """тестирование успешного выполнения декоратора"""
    example_success_function()
    captured = capsys.readouterr()
    assert captured.out == ('Starting example_success_function\n'
                            'example_success_function ok\n'
                            'Finished example_success_function\n'
                            '\n')


def test_err_decorators(capsys):
    """тестирование обработки исключений декоратора"""
    example_err_function()
    captured = capsys.readouterr()
    assert captured.out == ('Starting example_err_function\n'
                            'example_err_function error: Something went wrong!. Inputs: ()\n'
                            'Finished example_err_function\n'
                            '\n')
