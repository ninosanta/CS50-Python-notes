from plates import is_valid


def test_alpha():
    assert is_valid("HELLO") == True
    assert is_valid("hello") == True


def test_beginning():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1AB") == False
    assert is_valid("ab") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("AAA1234") == False
    assert is_valid("AAA123") == True


def test_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA22") == True


def test_notalphanum():
    assert is_valid("AAA,22") == False
    assert is_valid("Hello World") == False
    assert is_valid("Hello-World!") == False


def test_random():
    assert is_valid("GOODBYE") == False
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50!") == False
    assert is_valid("50") == False
