class Node:
    def __init__(self, value, next=None, random=None):
        self.value = value
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    mapping = {}
    node = head
    while node:
        mapping[node] = Node(node.value)
        node = node.next
    node = head
    while node:
        mapping[node].next = mapping.get(node.next)
        mapping[node].random = mapping.get(node.random)
        node = node.next
    return mapping[head]

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    a.next = b
    a.random = b
    b.random = b
    copied = copy_random_list(a)
    print(copied.value, copied.next.value, copied.random.value)
