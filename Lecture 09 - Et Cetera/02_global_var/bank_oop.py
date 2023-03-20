# Instance variables are global variables that are
# associated with a specific instance of a class.

class Account:
    def __init__(self):
        # instance attribute
        self._balance = 0  # _ indicates a "private" attribute

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()