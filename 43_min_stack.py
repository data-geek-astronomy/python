class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val):
        self._stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self):
        if not self._stack:
            return None
        val = self._stack.pop()
        if val == self._min_stack[-1]:
            self._min_stack.pop()
        return val

    def get_min(self):
        return self._min_stack[-1] if self._min_stack else None

if __name__ == "__main__":
    ms = MinStack()
    ms.push(3); ms.push(1); ms.push(2)
    print(ms.get_min())
