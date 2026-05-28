class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError

        self.capacity_ = capacity
        self.size_ = 0


    def __str__(self):
        return "🍪" * self.size_


    def deposit(self, n):
        if self.size_ + n > self.capacity_:
            raise ValueError

        self.size_ += n


    def withdraw(self, n):
        if n > self.size_:
            raise ValueError

        self.size_ -= n


    @property
    def capacity(self):
        return self.capacity_


    @property
    def size(self):
        return self.size_
