class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Size cannot be negative")
        if size > self.capacity:
            raise ValueError("Size cannot be greater than capacity")
        self._size = size


def main():
    jar = Jar(5)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)
    jar.withdraw(1)
    print(jar)
    jar.capacity = 10
    jar.deposit(8)
    print(jar)

if __name__ == "__main__":
    main()