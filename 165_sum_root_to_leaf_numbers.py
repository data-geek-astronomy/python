class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_numbers(root):
    def dfs(node, current):
        if not node:
            return 0
        current = current * 10 + node.value
        if not node.left and not node.right:
            return current
        return dfs(node.left, current) + dfs(node.right, current)

    return dfs(root, 0)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sum_numbers(root))
