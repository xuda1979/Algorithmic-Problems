from typing import Dict, List, Tuple
import heapq


def prim_mst(graph: Dict[int, List[Tuple[int, int]]], start: int = 0) -> List[Tuple[int, int, int]]:
    visited = set([start])
    pq = []
    for u, w in graph.get(start, []):
        heapq.heappush(pq, (w, start, u))
    mst = []
    while pq:
        w, v, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        mst.append((v, u, w))
        for nxt, wt in graph.get(u, []):
            if nxt not in visited:
                heapq.heappush(pq, (wt, u, nxt))
    return mst


def main() -> None:
    graph = {
        0: [(1, 4), (7, 8)],
        1: [(2, 8), (7, 11)],
        2: [(3, 7), (5, 4), (8, 2)],
        3: [(4, 9), (5, 14)],
        4: [(5, 10)],
        5: [(6, 2)],
        6: [(7, 1), (8, 6)],
        7: [(8, 7)],
        8: []
    }
    print("Prim MST:", prim_mst(graph, 0))


if __name__ == "__main__":
    main()
