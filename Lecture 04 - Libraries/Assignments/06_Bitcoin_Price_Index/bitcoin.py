import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python {sys.argv[0]} <n>")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit(f"Error: {sys.argv[1]} is not a `float` number")

    try:
        resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException as e:
        sys.exit(f"Error: {e}")

    value = float(resp.json()["bpi"]["USD"]["rate_float"])
    print(f"${(n * value):,.4f}")


if __name__ == "__main__":
    main()
