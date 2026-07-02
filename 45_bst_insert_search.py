class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    return search(root.left, value) if value < root.value else search(root.right, value)

if __name__ == "__main__":
    root = None
    for v in [5, 3, 8, 1, 4]:
        root = insert(root, v)
    print(search(root, 4), search(root, 10))
