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


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


def pre_order_recursive(root: TreeNode) -> None:
    if root is None:
        return
    print(root.value, end=" ")
    pre_order_recursive(root.left)
    pre_order_recursive(root.right)


def pre_order_iterative(root: TreeNode) -> None:
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def in_order_recursive(root: TreeNode) -> None:
    if root is None:
        return
    in_order_recursive(root.left)
    print(root.value, end=" ")
    in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
    if root is None:
        return
    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print(root.value, end=" ")


def breadth_first(root: TreeNode) -> None:
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)  # Dequeue
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    if node.value in visited:
        return
    visited.add(node.value)
    print(node.value, end=" ")
    for adjacent in node.adjacent:
        if adjacent.value not in visited:
            graph_depth_first_recursive(adjacent, visited)


def graph_depth_first_iterative(node: GraphNode) -> None:
    visited = set()
    stack = [node]
    while stack:
        current = stack.pop()
        if current.value in visited:
            continue
        visited.add(current.value)
        print(current.value, end=" ")
        for adjacent in current.adjacent:
            if adjacent.value not in visited:
                stack.append(adjacent)


def graph_breadth_first(node: GraphNode) -> None:
    visited = set()
    queue = [node]
    visited.add(node.value)
    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")
        for adjacent in current.adjacent:
            if adjacent.value not in visited:
                visited.add(adjacent.value)
                queue.append(adjacent)