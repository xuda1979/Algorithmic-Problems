from collections import defaultdict
from typing import Dict, List, Tuple, Optional

def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Optional[Dict[int, int]]:
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    vertices = list(graph.keys())
    for _ in range(len(vertices) - 1):
        for v in vertices:
            for u, w in graph.get(v, []):
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
    # detect negative cycle
    for v in vertices:
        for u, w in graph.get(v, []):
            if dist[v] + w < dist[u]:
                return None
    return dict(dist)


def main() -> None:
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, -2), (3, 5)],
        3: []
    }
    result = bellman_ford(graph, 0)
    if result is None:
        print("Negative cycle detected")
    else:
        print("Bellman-Ford distances from 0:", result)


if __name__ == "__main__":
    main()
