# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            self.root = None
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, values):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node
    
    def __iter__(self):
        current = self.root
        while current:
            yield str(current.value)
            current = current.next


# Implement the functions below

def list_sum(l: list[int]) -> int:
    """Returns the sum of elements using pop() recursively"""
    if not l:
        return 0
    return l.pop() + list_sum(l)


def digit_sum(n: int) -> int:
    """Returns the sum of digits using only mathematical operations"""
    if n == 0:
        return 0
    return (n % 10) + digit_sum(n // 10)


def tree_sum(root: TreeNode) -> int:
    """Returns the sum of all node values in the binary tree"""
    if root is None:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)


def tree_max(root: TreeNode) -> int:
    """Returns the maximum value in the binary tree"""
    if root is None:
        return float('-inf')
    left_max = tree_max(root.left)
    right_max = tree_max(root.right)
    return max(root.value, left_max, right_max)


def k_combinations(l: list[int], k: int) -> list[list[int]]:
    """Returns all possible combinations of k elements"""
    if k == 0:
        return [[]]
    if not l or k > len(l):
        return []
    with_first = [[l[0]] + combo for combo in k_combinations(l[1:], k - 1)]
    without_first = k_combinations(l[1:], k)
    return with_first + without_first


def all_strictly_increasing_sequences(k: int, n: int, **kwargs) -> list[list[int]]:
    """Returns all strictly increasing sequences of length k from first n natural numbers"""
    current = kwargs.get('current', [])
    start = kwargs.get('start', 1)
    if k == 0:
        return [current]
    if start > n:
        return []
    result = []
    for i in range(start, n + 1):
        if n - i >= k - 1:
            result.extend(all_strictly_increasing_sequences(
                k - 1, n, current=current + [i], start=i + 1
            ))
    return result


def create_pattern(n: int) -> list[int]:
    """Creates the pattern by subtracting 5 until ≤0, then adding 5 back to original"""
    if n <= 0:
        return [n]
    sub_pattern = create_pattern(n - 5)
    return [n] + sub_pattern + [n]


def find_middle(head: LinkedListNode) -> LinkedListNode:
    # Don't change this function
    return find_middle_rec(head)[1]


def find_middle_rec(head: LinkedListNode, n: int = 0) -> tuple[int, LinkedListNode]:
    """
    Returns (total_length, middle_node)
    Uses the hint: n counts nodes from left to right, 
    return value counts nodes from right to left during unwinding
    """
    if head is None:
        return 0, None
    rest_length, middle_candidate = find_middle_rec(head.next, n + 1)
    total_length = rest_length + 1
    current_pos = n
    middle_pos = total_length // 2
    if current_pos == middle_pos:
        return total_length, head
    elif middle_candidate is not None:
        return total_length, middle_candidate
    else:
        return total_length, None