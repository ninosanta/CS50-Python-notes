import pytest
from datetime import date
from seasons import seasons


def test_seasons_valid_inputs():
    today = date.today()
    assert seasons(f"{today.year}-{today.month}-{today.day}") == "Zero minutes"
    assert (
        seasons(f"{today.year-1}-{today.month}-{today.day}")
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        seasons(f"{today.year-2}-{today.month}-{today.day}")
        == "One million, fifty-one thousand, two hundred minutes"
    )


def test_seasons_invalid_inputs():
    with pytest.raises(SystemExit):
        seasons("Cat 2022-02-30")
        seasons("2023-02-30")
        seasons("01-01-2000")
        seasons("Mon 29 Jan 2001")
        seasons("2021,01,01")
