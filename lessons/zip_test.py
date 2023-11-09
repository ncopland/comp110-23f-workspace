"""Test my zip function."""

__author__ = "730659660"

from lessons.zip import zip


def test_edge_case() -> None:
    """Test the edge case scenario for zip function."""
    a = ["apple", "banana", "orange"]
    b = [1, 2, 3]
    result = zip(a, b)        
    expected = {"apple": 1, "banana": 2, "orange": 3}
    assert result == expected


def test_use_case_1() -> None:
    """Test use case scenario 1 for zip function."""
    a = ["1", "2", "3"]        
    b = [4, 5, 6]
    result = zip(a, b)
    expected = {"1": 4, "2": 5, "3": 6}
    assert result == expected


def test_use_case_2() -> None:
    """Test use case scenario 2 for zip function."""
    a = ["r", "b", "g"]
    b = [7, 8, 9]
    result = zip(a, b)
    expected = {"r": 7, "b": 8, "g": 9}
    assert result == expected