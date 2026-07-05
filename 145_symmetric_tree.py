class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_symmetric(root):
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b or a.value != b.value:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)

    return mirror(root, root)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    print(is_symmetric(root))
