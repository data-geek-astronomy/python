class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            return False
        idx = (self.front + self.size) % self.capacity
        self.queue[idx] = item
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

if __name__ == "__main__":
    cq = CircularQueue(3)
    cq.enqueue(1); cq.enqueue(2); cq.enqueue(3)
    print(cq.dequeue(), cq.dequeue())
