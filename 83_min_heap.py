import heapq

class MinHeap:
    def __init__(self):
        self._heap = []

    def push(self, val):
        heapq.heappush(self._heap, val)

    def pop(self):
        return heapq.heappop(self._heap) if self._heap else None

    def peek(self):
        return self._heap[0] if self._heap else None

if __name__ == "__main__":
    h = MinHeap()
    for v in [5, 3, 8, 1]:
        h.push(v)
    print(h.pop(), h.peek())
