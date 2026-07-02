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

def reverse_k_group(head, k):
    node = head
    count = 0
    while node and count < k:
        node = node.next
        count += 1
    if count < k:
        return head
    prev = None
    cur = head
    for _ in range(k):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    head.next = reverse_k_group(cur, k)
    return prev

if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print(to_list(reverse_k_group(head, 2)))
