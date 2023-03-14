from twttr import shorten


def test_all_vowels():
    assert shorten("aeiou") == ""


def test_all_consonants():
    assert shorten("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"


def test_alphadigit():
    assert shorten("Cs50AaU") == "Cs50"


def test_empty():
    assert shorten("") == ""


def test_all_caps():
    assert shorten("ZPLKAEIOU") == "ZPLK"
