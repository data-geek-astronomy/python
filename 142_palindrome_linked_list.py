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

def is_palindrome(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values == values[::-1]

if __name__ == "__main__":
    print(is_palindrome(build_list([1, 2, 2, 1])))
    print(is_palindrome(build_list([1, 2, 3])))
