class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

if __name__ == "__main__":
    a, b, c = Node(1), Node(2), Node(3)
    a.next, b.next, c.next = b, c, a
    print(has_cycle(a))
