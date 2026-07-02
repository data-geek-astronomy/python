class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop() if self._items else None

    def peek(self):
        return self._items[-1] if self._items else None

    def is_empty(self):
        return len(self._items) == 0

if __name__ == "__main__":
    s = Stack()
    s.push(1); s.push(2); s.push(3)
    print(s.pop(), s.peek())
