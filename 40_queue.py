from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.popleft() if self._items else None

    def is_empty(self):
        return len(self._items) == 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    print(q.dequeue(), q.dequeue())
