# Some operators such as `+` and `-` can be “overloaded” such 
# that they can have more abilities beyond simple arithmetic.

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        return Vault(
            self.galleons + other.galleons,
            self.sickles + other.sickles,
            self.knuts + other.knuts
        )

def main():
    potter = Vault(100, 50, 25)
    print("Potter:", potter)

    weasley = Vault(25, 50, 100)
    print("Weasley:", weasley)

    print("Total:", potter + weasley)




if __name__ == "__main__":
    main()