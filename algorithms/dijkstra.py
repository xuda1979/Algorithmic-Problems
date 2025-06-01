from collections import defaultdict
import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    dist = defaultdict(lambda: float('inf'))
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
    distances = dijkstra(graph, 0)
    print("Dijkstra distances from 0:", distances)


if __name__ == "__main__":
    main()
