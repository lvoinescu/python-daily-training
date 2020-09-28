# Implement a queue class using two stacks.
# A queue is a data structure that supports the FIFO protocol (First in = first out).
# Your class should support the enqueue and dequeue methods like a standard queue.


class NaiveQueue:

    def __init__(self):
        self.pivot = []
        self.storage = []

    def enqueue(self, val):
        while len(self.storage) > 0:
            self.pivot.append(self.storage.pop())

        self.storage.append(val)

        while len(self.pivot) > 0:
            self.storage.append(self.pivot.pop())

    def dequeue(self):
        return self.storage.pop()


class OptimizedQueue:

    def __init__(self):
        self.accumulator = []
        self.popper = []

    def enqueue(self, val):
        if len(self.accumulator) == 0:
            self.accumulator.append(val)
        else:
            if len(self.accumulator) == 1:
                self.accumulator, self.popper = self.popper, self.accumulator
                self.accumulator.append(val)
            else:
                self.accumulator.append(val)

    def dequeue(self):
        if len(self.popper) == 1:
            return self.popper.pop()

        if len(self.accumulator) == 1:
            return self.accumulator.pop()

        element = self.popper.pop()
        count = len(self.accumulator) - 1
        i = 0
        while i < count:
            self.popper.append(self.accumulator.pop())
            self.accumulator, self.popper = self.popper, self.accumulator
            i -= 1
        return element


q = NaiveQueue()
q.enqueue(1)
print(q.dequeue())
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
# 1 2 3


p = OptimizedQueue()
p.enqueue(1)
print(p.dequeue())
p.enqueue(2)
p.enqueue(3)
print(p.dequeue())
print(p.dequeue())
# 1 2 3
