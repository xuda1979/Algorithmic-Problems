from collections import deque
from typing import Dict, List, Tuple

def bfs(graph: Dict[int, List[Tuple[int, int]]], start: int) -> List[int]:
    visited = set([start])
    order = []
    queue = deque([start])
    while queue:
        v = queue.popleft()
        order.append(v)
        for u, _ in graph.get(v, []):
            if u not in visited:
                visited.add(u)
                queue.append(u)
    return order


def main() -> None:
    graph = {
        0: [(1, 1), (2, 1)],
        1: [(3, 1)],
        2: [(3, 1)],
        3: []
    }
    order = bfs(graph, 0)
    print("BFS order starting from 0:", order)


if __name__ == "__main__":
    main()
