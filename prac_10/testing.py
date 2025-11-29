"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"


    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car.fuel == 0, "Car default fuel should be 0"


    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    car = Car(fuel=10)
    assert car.fuel == 10, "Car should set fuel correctly when given"
    print("All tests passed")

def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a proper sentence:
    - First letter capitalised
    - Ends with a single period

    >>> format_phrase_as_sentence("hello")
    'Hello.'
    >>> format_phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_as_sentence("python")
    'Python.'
    """
    phrase = phrase.strip()
    if not phrase:
        return "."
    phrase = phrase[0].upper() + phrase[1:]
    if not phrase.endswith("."):
        phrase += "."
    return phrase

run_tests()

doctest.testmod()
