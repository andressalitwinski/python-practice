import pytest
from fuel_reimp import convert, gauge

def test_convert_fractions():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100


def test_invalid_parameters():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("1/b")
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ValueError):
        convert("1.5/2")
    with pytest.raises(ValueError):
        convert("1/2.5")


def test_negative_numbers():
    with pytest.raises(ValueError):
        convert("-1/5")
    with pytest.raises(ValueError):
        convert("1/-2")


def test_x_gt_y():
    with pytest.raises(ValueError):
        convert("3/2")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge():
    assert gauge(2) == "2%"
    assert gauge(38) == "38%"
    assert gauge(98) == "98%"
