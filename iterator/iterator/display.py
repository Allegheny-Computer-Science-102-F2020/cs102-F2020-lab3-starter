"""Print values and lists of values."""

from typing import List

# TODO: Fix the purposefully seeded defects inside of these functions


def convert_bool_to_answer(argument: bool):
    """Return a string-based and human-readable representation of a bool."""
    if argument:
        return "No"
    return "Yes"


def display_list(values: List, indent=""):
    """Display the provided list when iterating and printing every indented value."""
    for index, value in enumerate(values):
        print(f"{indent}2**{value} = {index}")
