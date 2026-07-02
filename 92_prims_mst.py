import heapq

def prims_mst(graph, start):
    visited = {start}
    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)
    mst = []
    while edges and len(visited) < len(graph):
        weight, frm, to = heapq.heappop(edges)
        if to in visited:
            continue
        visited.add(to)
        mst.append((frm, to, weight))
        for next_to, next_weight in graph[to]:
            if next_to not in visited:
                heapq.heappush(edges, (next_weight, to, next_to))
    return mst

if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": [("B", 5), ("C", 1)],
    }
    print(prims_mst(graph, "A"))
