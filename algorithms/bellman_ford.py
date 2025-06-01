from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import math


def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Optional[Dict[int, float]]:
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    vertices = list(graph.keys())
    for _ in range(len(vertices) - 1):
        for v in vertices:
            for u, w in graph.get(v, []):
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
    for v in vertices:
        for u, w in graph.get(v, []):
            if dist[v] + w < dist[u]:
                return None
    return dict(dist)


def main() -> None:
    graph = {
        0: [(1, 1), (2, 4)],
        1: [(2, -3), (3, 2)],
        2: [(3, 3)],
        3: []
    }
    print("Bellman-Ford:", bellman_ford(graph, 0))


if __name__ == "__main__":
    main()
