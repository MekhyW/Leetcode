class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []  # List of Nodes this node points to

def has_route(start_node: GraphNode, end_node: GraphNode) -> bool:
    if start_node is None or end_node is None:
        return False
    if start_node == end_node:
        return True
    #BFS
    visited = set([start_node])
    queue = [start_node]
    while queue:
        current_node = queue.pop(0)
        for neighbor in current_node.adjacent:
            if neighbor == end_node:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False