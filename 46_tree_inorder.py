class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(inorder(root))
