class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

def nth_to_last(head: Node, k: int) -> Node:
    if not head or k < 1:
        return None
    p1 = p2 = head
    for _ in range(k):
        if not p1:
            return None
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2
