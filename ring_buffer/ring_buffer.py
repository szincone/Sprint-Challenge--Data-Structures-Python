class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        # clean way to reset the cur index when it reaches max length
        self.current = (self.current + 1) % self.capacity
        return self.storage

    def get(self):
        return [x for x in self.storage if x is not None]
