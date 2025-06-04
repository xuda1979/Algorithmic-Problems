def kruskal_mst(vertices, edges):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    mst = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if union(u, v):
            mst.append((u, v, w))
    return mst


def main():
    vertices = [1, 2, 3, 4]
    edges = [(1, 2, 1), (2, 3, 2), (3, 4, 1), (4, 1, 2), (1, 3, 2)]
    print(kruskal_mst(vertices, edges))


if __name__ == '__main__':
    main()
