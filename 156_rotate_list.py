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

def rotate_right(head, k):
    if not head or not head.next:
        return head
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    k %= length
    if k == 0:
        return head
    tail.next = head
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head

if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print(to_list(rotate_right(head, 2)))
