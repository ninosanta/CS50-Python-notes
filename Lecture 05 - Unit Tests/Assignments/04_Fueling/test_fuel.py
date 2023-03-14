from fuel import gauge, convert
import pytest


def test_convert_zero_division():
    with pytest.raises(SystemExit):
        convert("1/0")
        convert("0/0")


def test_convert_X_gt_Y():
    with pytest.raises(SystemExit):
        convert("2/1")
        convert("-1/1")


def test_convert_invalid_values():
    with pytest.raises(SystemExit):
        convert("1")
        convert("1/")
        convert("/1")
        convert("1/2/3")
        convert("cat/bat")
        convert("hello, world")


def test_convert_legit_values():
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("1/4") == 25
    assert convert("1/5") == 20
    assert convert("1/6") == 17
    assert convert("3/4") == 75
    assert convert("0/1") == 0


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_mid_values():
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(50) == "50%"
