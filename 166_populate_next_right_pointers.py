class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    if not root:
        return None
    leftmost = root
    while leftmost.left:
        node = leftmost
        while node:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            node = node.next
        leftmost = leftmost.left
    return root

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    connect(root)
    print(root.left.next.value, root.left.right.next.value)
