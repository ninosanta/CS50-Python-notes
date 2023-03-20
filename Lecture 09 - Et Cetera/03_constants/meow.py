MEOWS = 3  # convention: constants are all caps...
           # based on the honor system

for _ in range(MEOWS):
    print("meow")


# Another convention
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(self.MEOWS):
            print("meow")

cat = Cat()
cat.meow()