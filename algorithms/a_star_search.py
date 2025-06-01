from typing import Dict, List, Tuple, Callable, Optional
import heapq


def a_star_search(
    graph: Dict[int, List[Tuple[int, int]]],
    start: int,
    goal: int,
    heuristic: Callable[[int], int]
) -> Optional[List[int]]:
    open_set = [(heuristic(start), 0, start, [])]
    visited = set()
    while open_set:
        est, cost, node, path = heapq.heappop(open_set)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neigh, weight in graph.get(node, []):
            if neigh not in visited:
                new_cost = cost + weight
                heapq.heappush(open_set, (new_cost + heuristic(neigh), new_cost, neigh, path))
    return None


def main() -> None:
    graph = {
        0: [(1, 1), (2, 3)],
        1: [(3, 1)],
        2: [(3, 1)],
        3: []
    }
    heuristic = lambda x: 0
    print("A* path:", a_star_search(graph, 0, 3, heuristic))


if __name__ == "__main__":
    main()
