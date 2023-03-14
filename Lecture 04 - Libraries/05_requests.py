# Python, through the `requests` package, has the ability
# to download and embed code from third party APIs that
# are somewhere on a server.
# `requests` is a package that allows to make HTTP requests
# using Python code.

# iTunes API:
#   Visiting https://itunes.apple.com/search?entity=song&limit=1&term=weezer
#   will result in the download of a JSON file containing all the information
#   about the first song that iTunes finds when searching for "weezer".
import requests
import sys
import json


def itunes():
    if len(sys.argv) != 2:
        sys.exit(f"Usage: python {sys.argv[0]} <name of a band>")

    # GET request to the iTunes web server
    response = requests.get(
        f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}"
    )
    # print(response.json())  # the JSON file is converted to a Python dictionary... not very readable
    # print(json.dumps(response.json(), indent=2))  # just to make it more readable
    obj = response.json()
    for result in obj["results"]:
        print(f"Artist: {result['artistName']}")
        print(f"Song: {result['trackName']}")
        print(f"Album: {result['collectionName']}")
        print(f"Link: {result['trackViewUrl']}", end="\n\n")


def main():
    itunes()


if __name__ == "__main__":
    main()
