# https://pypi.org/project/validator-collection/
# https://pypi.org/project/validators/

from validator_collection import checkers
import validators

def main():
    print("Valid" if validate(input("What's your email address? ")) else "Invalid")


def validate(email):
    return checkers.is_email(email) and validators.email(email)