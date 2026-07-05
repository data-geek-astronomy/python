class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def flatten(root):
    node = root
    while node:
        if node.left:
            rightmost = node.left
            while rightmost.right:
                rightmost = rightmost.right
            rightmost.right = node.right
            node.right = node.left
            node.left = None
        node = node.right
    return root

def to_list(root):
    result = []
    while root:
        result.append(root.value)
        root = root.right
    return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(5)
    print(to_list(flatten(root)))
