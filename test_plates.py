import pytest
import plates


def test_check_len():
    assert plates.check_len("1") is False
    assert plates.check_len("12345678") is False
    assert plates.check_len("12") is True
    assert plates.check_len("123456") is True


def test_no_marks():
    assert plates.no_marks("a3!") is False
    assert plates.no_marks("ab23") is True


def test_starts_with_letters():
    assert plates.starts_with_letters("as3") is True
    assert plates.starts_with_letters("XYZ12") is True
    assert plates.starts_with_letters("z345") is False
    assert plates.starts_with_letters("1as") is False


def test_check_numbers():
    assert plates.check_numbers("AAA222") is True
    assert plates.check_numbers("AAA22A") is False
    assert plates.check_numbers("XYZ02") is False


# ---------- valid ----------


def test_min_length_letters_only():
    assert plates.is_valid("AB") is True


def test_max_length_letters_only():
    assert plates.is_valid("ABCDEF") is True


def test_letters_then_numbers():
    assert plates.is_valid("CS50") is True
    assert plates.is_valid("AB123") is True


# ---------- invalid ----------


def test_too_short():
    assert plates.is_valid("A") is False


def test_too_long():
    assert plates.is_valid("ABCDEFG") is False


def test_contains_punctuation():
    assert plates.is_valid("AB-12") is False


def test_contains_space():
    assert plates.is_valid("AB 12") is False


def test_does_not_start_with_two_letters():
    assert plates.is_valid("1A234") is False
    assert plates.is_valid("A123") is False


def test_number_starts_with_zero():
    assert plates.is_valid("AB012") is False


def test_letter_after_number():
    assert plates.is_valid("AB12C") is False


def test_only_numbers():
    assert plates.is_valid("1234") is False


# ---------- Parametrized  ----------


@pytest.mark.parametrize(
    "plate, expected",
    [
        ("AA", True),
        ("AAA222", True),
        ("AB1234", True),
        ("AB0", False),
        ("AB01", False),
        ("AB12C", False),
        ("A1", False),
        ("12AB", False),
        ("AB!", False),
        ("", False),
    ],
)
def test_various_plates(plate, expected):
    assert plates.is_valid(plate) is expected
