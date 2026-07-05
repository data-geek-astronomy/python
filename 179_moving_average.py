from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.window = deque()
        self.total = 0

    def next(self, val):
        self.window.append(val)
        self.total += val
        if len(self.window) > self.size:
            self.total -= self.window.popleft()
        return self.total / len(self.window)

if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1), ma.next(10), ma.next(3), ma.next(5))
