from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

if __name__ == "__main__":
    s = MyStack()
    s.push(1); s.push(2); s.push(3)
    print(s.pop(), s.top())
