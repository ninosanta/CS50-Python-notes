from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello, Kramer") == 0


def test_h():
    assert value("h") == 20
    assert value("H") == 20
    assert value("How you doing?") == 20


def test_other():
    assert value("other") == 100
    assert value("What's up Kramer?") == 100
