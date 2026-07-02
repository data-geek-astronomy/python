class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        preorder(root.left, result)
        preorder(root.right, result)
    return result

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(preorder(root))
