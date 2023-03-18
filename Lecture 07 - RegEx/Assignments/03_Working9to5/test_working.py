import pytest
from working import convert


def test_valid_inputs():
    assert convert("1:00 PM to 2:00 PM") == "13:00 to 14:00"
    assert convert("1:00 PM to 2:00 AM") == "13:00 to 02:00"
    assert convert("9 AM to 10 PM") == "09:00 to 22:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_inputs():
    with pytest.raises(SystemExit):
        convert("9:60 AM to 5:60 PM")
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")
        convert("from 1:00 PM up to 2:00 PM")
