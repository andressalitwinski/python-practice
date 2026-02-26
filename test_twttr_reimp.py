import pytest
from twttr_reimp import shorten


def test_shorten_mmixed():
    assert shorten("Apple") == "ppl"
    assert shorten("bAnanA") == "bnn"


def test_shorten_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""


def test_shorten_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""


def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("CS50") == "CS50"


def test_numbers_and_symbols():
    assert shorten("h3ll0!") == "h3ll0!"
    assert shorten("1234") == "1234"


def test_empty_string():
    assert shorten("") == ""


def test_whitespace_preserved():
    assert shorten("a e i o u") == "    "


def test_phrase():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Hello, World!", "Hll, Wrld!"),
        ("CS50", "CS50"),
        ("PYTHON", "PYTHN"),
        ("123 AEIOU 456", "123  456"),
    ],
)
def test_various_inputs(input_text, expected):
    assert shorten(input_text) == expected