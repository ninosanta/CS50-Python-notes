# Bitcoin Price Index

Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called `bitcoin.py`, implement a program that:

* Expects the user to specify as a command-line argument the number of Bitcoins, `n`, that they would like to buy. If that argument cannot be converted to a `float`, the program should exit via `sys.exit` with an error message.
* Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a `JSON` object, among whose nested keys is the current price of Bitcoin as a `float`. Be sure to catch any exceptions, as with code like:
    ```python
    import requests

    try:
        ...
    except requests.RequestException:
        ...
    ```
Outputs the current cost of `n` Bitcoins in USD to four decimal places, using `,` as a thousands separator.

## How to Test

Here’s how to test your code manually:

* Run your program with `python bitcoin.py`. Your program should use `sys.exit` to exit with an error message:
    ```shell
    Missing command-line argument   
    ```
* Run your program with `python bitcoin.py` cat. Your program should use `sys.exit` to exit with an error message:
    ```shell
    Command-line argument is not a number
    ```
* Run your program with `python bitcoin.py 1`. Your program should output the price of a single Bitcoin to four decimal places, using `,` as a thousands separator.
* Run your program with `python bitcoin.py 2`. Your program should output the price of two Bitcoin to four decimal places, using `,` as a thousands separator.
* Run your program with `python bitcoin.py 2.5`. Your program should output the price of 2.5 Bitcoin to four decimal places, using `,` as a thousands separator.