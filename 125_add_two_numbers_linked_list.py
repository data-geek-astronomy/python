class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_list(values):
    head = tail = None
    for v in values:
        node = Node(v)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def add_two_numbers(l1, l2):
    dummy = tail = Node(0)
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.value if l1 else 0
        v2 = l2.value if l2 else 0
        total = v1 + v2 + carry
        carry, digit = divmod(total, 10)
        tail.next = Node(digit)
        tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

if __name__ == "__main__":
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    print(to_list(add_two_numbers(l1, l2)))
