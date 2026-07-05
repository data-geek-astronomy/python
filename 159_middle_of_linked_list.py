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

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print(middle_node(head).value)
