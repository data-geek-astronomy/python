class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def range_sum_bst(root, low, high):
    if not root:
        return 0
    if root.value < low:
        return range_sum_bst(root.right, low, high)
    if root.value > high:
        return range_sum_bst(root.left, low, high)
    return root.value + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    print(range_sum_bst(root, 7, 15))
