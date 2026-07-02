import heapq

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

def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.value, i, node))
    dummy = tail = Node(0)
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.value, i, node.next))
    return dummy.next

if __name__ == "__main__":
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    print(to_list(merge_k_lists(lists)))
