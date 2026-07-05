class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def path_sum(root, target):
    result = []

    def backtrack(node, remaining, path):
        if not node:
            return
        path.append(node.value)
        remaining -= node.value
        if not node.left and not node.right and remaining == 0:
            result.append(path[:])
        else:
            backtrack(node.left, remaining, path)
            backtrack(node.right, remaining, path)
        path.pop()

    backtrack(root, target, [])
    return result

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    print(path_sum(root, 22))
