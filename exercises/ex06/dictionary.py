"""Dictionary Stuff."""

__author__ = "730659660"


def invert(inv: dict[str, str]) -> dict[str, str]:
    """Inverts list."""
    new_dict: dict[str, str] = {}
    for item in inv:
        if inv[item] in new_dict:
            raise KeyError("identical")
        else:
            new_dict[inv[item]] = item
    
    return new_dict


def favorite_color(inp: dict[str, str]) -> str:
    """Finds most common color."""
    hash: dict[str, int] = {}
    color = ""
    i = 0
    for item, col in inp.items():
        if col in hash:
            hash[col] += 1
        else:
            hash[col] = 1

    if hash[col] >= i:
        i = hash[col]
        color = col

    return color


def count(list1: list[str]) -> dict[str, int]:
    """Counts stuff."""
    count_dict: dict[str, int] = {}
    for value in list1:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Alphabetical order of a list."""
    alphabet_dict: dict[str, list[str]] = {}
    for word in list1:
        first_letter = word[0].lower()
        if first_letter not in alphabet_dict:
            alphabet_dict[first_letter] = [word]
        else: 
            alphabet_dict[first_letter].append(word)
    return alphabet_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance."""
    if day in attendance:
        if student in attendance[day]:
            student = student
        else:
            attendance[day].append(student)
    else:
        attendance[day] = [student]
    return attendance