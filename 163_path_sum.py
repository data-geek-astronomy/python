class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return target == root.value
    remaining = target - root.value
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    print(has_path_sum(root, 20))
