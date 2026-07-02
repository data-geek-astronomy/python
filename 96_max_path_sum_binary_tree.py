class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_path_sum(root):
    best = float("-inf")

    def helper(node):
        nonlocal best
        if not node:
            return 0
        left = max(helper(node.left), 0)
        right = max(helper(node.right), 0)
        best = max(best, node.value + left + right)
        return node.value + max(left, right)

    helper(root)
    return best

if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(max_path_sum(root))
