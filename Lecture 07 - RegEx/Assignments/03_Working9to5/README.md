# Working 9 to 5

Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table:
    Just as “12:00 AM” in 12-hour format would be “00:00” in 24-hour format, so would “12:01 AM” through “12:59 AM” be “00:01” through “00:59”, respectively.
    
|12-hour|24-hour|
|:-----:|:-----:|
|12:00 AM|00:00|
|1:00 AM|01:00|
|2:00 AM|02:00|
|3:00 AM|03:00|
|4:00 AM|04:00|
|5:00 AM|05:00|
|6:00 AM|06:00|
|7:00 AM|07:00|
|8:00 AM|08:00|
|9:00 AM|09:00|
|10:00 AM|10:00|
|11:00 AM|11:00|
|12:00 PM|12:00|
|1:00 PM|13:00|
|2:00 PM|14:00|
|3:00 PM|15:00|
|4:00 PM|16:00|
|5:00 PM|17:00|
|6:00 PM|18:00|
|7:00 PM|19:00|
|8:00 PM|20:00|
|9:00 PM|21:00|
|10:00 PM|22:00|
|11:00 PM|23:00|
|12:00 AM|00:00|

In a file called `working.py`, implement a function called `convert` that expects a `str` in either of the 12-hour formats below and returns the corresponding `str` in 24-hour format (i.e., `9:00 to 17:00`). Expect that `AM` and `PM` will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily `9:00 AM` and `5:00 PM` specifically.

* `9:00 AM to 5:00 PM`
* `9 AM to 5 PM`

Raise a `ValueError` instead if the input to `convert` is not in either of those formats or if either time is invalid (e.g., `12:60 AM`, `13:00 PM`, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., `5:00 PM to 9:00 AM`).

Structure `working.py` as follows, wherein you’re welcome to modify `main` and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use `re` and/or `sys`.

```python
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
```
Either before or after you implement `convert` in `working.py`, additionally implement, in a file called `test_working.py`, three or more functions that collectively test your implementation of `convert` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

    pytest test_working.py
