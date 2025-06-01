import heapq
from typing import Dict, List, Tuple

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
        0: [(1, 4), (2, 3)],
        1: [(0, 4), (2, 1), (3, 2)],
        2: [(0, 3), (1, 1), (3, 4)],
        3: [(1, 2), (2, 4)]
    }
    mst = prim_mst(graph, 0)
    print("Prim MST edges:", mst)


if __name__ == "__main__":
    main()
