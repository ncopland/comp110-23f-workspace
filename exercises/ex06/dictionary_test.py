"""Test cases for the dictionary methods."""

from exercises.ex06.dictionary import invert, count, favorite_color, alphabetizer, update_attendance

__author__ = "730659660"


def test_invert_use_case1() -> None:
    """Test the use case scenario for zip function."""
    a = {"apple": "1", "banana": "2", "orange": "3"} 
    expected = {"1": "apple", "2": "banana", "3": "orange"}
    assert invert(a) == expected


def test_invert_use_case_2() -> None:
    """Test use case scenario 2 for invert function."""
    a = {"r": "a", "b": "d"}
    expected = {"a": "r", "d": "b"}
    assert invert(a) == expected


def test_invert_edge_case() -> None:
    """Test the edge case scenario for invert function."""
    a = {"apple": "1", "banana": "1", "orange": "3"}
    expected = {"1": "banana", "3": "orange"}
    assert invert(a) == expected


def test_favorite_color_use_case1() -> None:
    """Test the use case scenario for favorite color function."""
    a = {"1": "blue", "2": "blue", "3": "blue"}
    expected = "blue"
    assert favorite_color(a) == expected


def test_favorite_color_use_case_2() -> None:
    """Test use case scenario 2 for favorite color function."""
    a = {"1": "purble", "2": "blue"}
    expected = ""
    assert favorite_color(a) == expected


def test_favorite_color_edge_case() -> None:
    """Test the edge case scenario for favorite color function."""
    a = {"1": "", "2": "", "3": "purple"}
    expected = ""
    assert favorite_color(a) == expected


def test_count_use_case1() -> None:
    """Test the use case scenario for count function."""
    a = ["apple", "banana", "banana", "orange", "orange", "orange"]
    expected = {"apple": 1, "banana": 2, "orange": 3}
    assert count(a) == expected


def test_count_use_case_2() -> None:
    """Test use case scenario 2 for count function."""
    a = ["r", "b"]
    expected = {"r": 1, "b": 1}
    assert count(a) == expected


def test_count_edge_case() -> None:
    """Test the edge case scenario for count function."""
    a = ["apple", "orange", "banana", "orange"]
    expected = {"apple": 1, "orange": 2, "banana": 1}
    assert count(a) == expected


def test_alphabetizer_use_case1() -> None:
    """Test the use case scenario for alphabetizer function."""
    a = ["apple", "banana", "banana", "orange", "orange", "orange"]
    expected = {"a": ["apple"], "b": ["banana", "banana"], "o": ["orange", "orange", "orange"]}
    assert alphabetizer(a) == expected


def test_alphabetizer_use_case_2() -> None:
    """Test use case scenario 2 for alphabetizer function."""
    a = ["r", "b"]
    expected = {"r": ["r"], "b": ["b"]}
    assert alphabetizer(a) == expected


def test_alphabetizer_edge_case() -> None:
    """Test the edge case scenario for alphabetizer function."""
    a = ["apple", "orange", "banana", "orange"]
    expected = {"a": ["apple"], "o": ["orange", "orange"], "b": ["banana"]}
    assert alphabetizer(a) == expected


def test_update_attendance_use_case1() -> None:
    """Test the use case scenario for update_attendance function."""
    a = {"a": ["apple"], "o": ["orange"], "b": ["banana"]}
    result = update_attendance(a, "o", "orange")
    expected = {"a": ["apple"], "o": ["orange", "orange"], "b": ["banana"]}
    assert result == expected


def test_update_attendance_use_case_2() -> None:
    """Test use case scenario 2 for update_attendance function."""
    a = {"a": ["apple"], "o": ["orange", "orange"], "b": ["banana"]}
    result = update_attendance(a, "d", "pear")
    expected = {"a": ["apple"], "o": ["orange", "orange"], "b": ["banana"], "d": ["pear"]}
    assert result == expected


def test_update_attendance_edge_case() -> None:
    """Test the edge case scenario for update_attendance function."""
    a = {"a": ["apple"], "o": ["orange", "orange"], "b": ["banana"]}
    result = update_attendance(a, "d", "orange")
    expected = {"a": ["apple"], "o": ["orange", "orange"], "b": ["banana"], "d": ["pear"]}
    assert result == expected