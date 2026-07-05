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

def partition(head, x):
    before_head = before = Node(0)
    after_head = after = Node(0)
    while head:
        if head.value < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next

if __name__ == "__main__":
    head = build_list([1, 4, 3, 2, 5, 2])
    print(to_list(partition(head, 3)))
