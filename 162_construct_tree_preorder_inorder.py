class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
    return root

def preorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)
    return result

if __name__ == "__main__":
    tree = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(preorder_traversal(tree))
