class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return "#"
    return f"{root.value},{serialize(root.left)},{serialize(root.right)}"

def deserialize(data):
    values = iter(data.split(","))

    def build():
        val = next(values)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    data = serialize(root)
    restored = deserialize(data)
    print(data, "->", restored.value, restored.left.value, restored.right.value)
