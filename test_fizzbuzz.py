import pytest
from fizzbuzz import FizzBuzz, ERR_INVALID_RANGE, ERR_INVALID_TYPE


def test_inputs_not_integers():
    input_start = 10
    input_end = "asd"

    with pytest.raises(ValueError, match=ERR_INVALID_TYPE):
        FizzBuzz(input_start, input_end).run()


def test_integer_not_in_range():
    input_start = 30
    input_end = 150

    with pytest.raises(ValueError, match=ERR_INVALID_RANGE):
        FizzBuzz(input_start, input_end).run()


def test_negative_inputs():
    input_start = -10
    input_end = -20

    with pytest.raises(ValueError, match=ERR_INVALID_RANGE):
        FizzBuzz(input_start, input_end).run()


def test_end_integer_is_lower():
    input_start = 15
    input_end = 10

    result = FizzBuzz(input_start, input_end).run()
    assert result == ["10: buzz ", "11: ", "12: fizz ", "13: ", "14: "]


def test_start_integer_is_lower():
    input_start = 10
    input_end = 15

    result = FizzBuzz(input_start, input_end).run()
    assert result == ["10: buzz ", "11: ", "12: fizz ", "13: ", "14: "]
