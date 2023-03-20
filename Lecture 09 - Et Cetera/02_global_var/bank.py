# In Python can be accessed from anywhere in the program
# in read-only mode, i.e., you can't change the value of
# a global variable but you can read it.
#
# It turns out that they can be changed, but only if you
# declare them as `global` variables in the other functions.


balance = 0


def deposit(amount):
    global balance
    balance += amount


def withdraw(amount):
    global balance
    balance -= amount


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


if __name__ == "__main__":
    main()
