from typing import List, Tuple

def kruskal_mst(vertices: List[int], edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(v: int) -> int:
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(u: int, v: int) -> bool:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        if rank[ru] < rank[rv]:
            parent[ru] = rv
        elif rank[ru] > rank[rv]:
            parent[rv] = ru
        else:
            parent[rv] = ru
            rank[ru] += 1
        return True

    mst = []
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if union(u, v):
            mst.append((u, v, w))
    return mst


def main() -> None:
    vertices = [0, 1, 2, 3]
    edges = [
        (0, 1, 4),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 3, 4)
    ]
    mst = kruskal_mst(vertices, edges)
    print("Kruskal MST edges:", mst)


if __name__ == "__main__":
    main()
