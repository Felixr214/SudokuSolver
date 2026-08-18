class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count = self.count + 1

    def sub(self):
        self.count = self.count - 1

    def reset(self):
        self.count = 0
