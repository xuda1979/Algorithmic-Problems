from collections import defaultdict, deque
from typing import Dict, List, Tuple


def topological_sort(graph: Dict[int, List[Tuple[int, int]]]) -> List[int]:
    indeg = defaultdict(int)
    for v in graph:
        for u, _ in graph[v]:
            indeg[u] += 1
    queue = deque([v for v in graph if indeg[v] == 0])
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for u, _ in graph.get(v, []):
            indeg[u] -= 1
            if indeg[u] == 0:
                queue.append(u)
    if len(order) != len(graph):
        raise ValueError("Graph has a cycle")
    return order


def main() -> None:
    graph = {
        5: [(2, 1), (0, 1)],
        4: [(0, 1), (1, 1)],
        2: [(3, 1)],
        3: [(1, 1)],
        1: [],
        0: []
    }
    print("Topological order:", topological_sort(graph))


if __name__ == "__main__":
    main()
