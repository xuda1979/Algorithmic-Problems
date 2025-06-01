from collections import defaultdict
from typing import Dict, List, Tuple
import heapq
import math


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, float]:
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, w in graph.get(v, []):
            nd = d + w
            if nd < dist[u]:
                dist[u] = nd
                heapq.heappush(pq, (nd, u))
    return dict(dist)


def main() -> None:
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print("Shortest paths:", dijkstra(graph, 0))


if __name__ == "__main__":
    main()
