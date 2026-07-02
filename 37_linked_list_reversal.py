class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_list(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

def to_list(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

if __name__ == "__main__":
    head = build_list([1, 2, 3, 4])
    print(to_list(reverse_list(head)))
