from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def get_hits(self, timestamp):
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)

if __name__ == "__main__":
    hc = HitCounter()
    hc.hit(1)
    hc.hit(2)
    hc.hit(3)
    print(hc.get_hits(4))
    hc.hit(300)
    print(hc.get_hits(300))
    print(hc.get_hits(301))
