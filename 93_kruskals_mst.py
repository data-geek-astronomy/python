class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        self.parent[root_y] = root_x
        return True

def kruskals_mst(num_nodes, edges):
    edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(num_nodes)
    mst = []
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
    return mst

if __name__ == "__main__":
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    print(kruskals_mst(4, edges))
