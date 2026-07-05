class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_intersection_node(head_a, head_b):
    a, b = head_a, head_b
    while a is not b:
        a = a.next if a else head_b
        b = b.next if b else head_a
    return a

if __name__ == "__main__":
    common = Node(8)
    common.next = Node(10)
    a = Node(4)
    a.next = Node(1)
    a.next.next = common
    b = Node(5)
    b.next = Node(6)
    b.next.next = Node(1)
    b.next.next.next = common
    result = get_intersection_node(a, b)
    print(result.value if result else None)
