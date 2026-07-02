from collections import deque

def bfs(graph, start):
    visited, order = set([start]), []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

if __name__ == "__main__":
    graph = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
    print(bfs(graph, 1))
