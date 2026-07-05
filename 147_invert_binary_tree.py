class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def to_preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        to_preorder(root.left, result)
        to_preorder(root.right, result)
    return result

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    print(to_preorder(invert_tree(root)))
