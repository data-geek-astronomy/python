from collections import deque

def topological_sort(graph, num_nodes):
    in_degree = [0] * num_nodes
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = deque([n for n in range(num_nodes) if in_degree[n] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_nodes else []

if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print(topological_sort(graph, 4))
