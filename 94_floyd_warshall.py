def floyd_warshall(graph, num_nodes):
    dist = [[float("inf")] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        dist[i][i] = 0
    for u, v, weight in graph:
        dist[u][v] = weight
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    edges = [(0, 1, 3), (1, 2, 1), (0, 2, 10)]
    for row in floyd_warshall(edges, 3):
        print(row)
