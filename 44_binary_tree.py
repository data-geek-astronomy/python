class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(root.value, root.left.value, root.right.value)
