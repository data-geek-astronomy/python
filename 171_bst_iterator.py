class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def has_next(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        self._push_left(node.right)
        return node.value

if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    it = BSTIterator(root)
    print([it.next() for _ in range(4)])
