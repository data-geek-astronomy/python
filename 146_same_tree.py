class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.value != q.value:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.left = TreeNode(2)
    print(is_same_tree(p, q))
