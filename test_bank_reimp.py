import pytest
from bank_reimp import value


def test_hello():
    assert value("Hello") == 0
    assert value("HellO") == 0
    assert value("hEllo") == 0


def test_hello_with_text_after():
    assert value("hello there") == 0


def test_h():
    assert value("Hey") == 20
    assert value("HI") == 20
    assert value("hollA") == 20


def test_not_h():
    assert value("Morning") == 100
    assert value("good morning") == 100
    assert value("WeLcOmE") == 100


def test_empty_string():
    assert value("") == 100

def test_leading_spaces():
    assert value("  Hello") == 0
    assert value("   heY") == 20
    assert value(" welcome") == 100

@pytest.mark.parametrize(
    "greeting, expected",
    [
        ("hello!", 0),
        ("HELLO", 0),
        ("h", 20),
        ("how are you?", 20),
        ("welcome", 100),
        ("123", 100),
    ],
)
def test_various_inputs(greeting, expected):
    assert value(greeting.lower()) == expected
