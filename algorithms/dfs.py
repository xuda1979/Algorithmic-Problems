from typing import Dict, List, Tuple

def dfs(graph: Dict[int, List[Tuple[int, int]]], start: int) -> List[int]:
    visited = set()
    order = []

    def _dfs(v: int) -> None:
        visited.add(v)
        order.append(v)
        for u, _ in graph.get(v, []):
            if u not in visited:
                _dfs(u)

    _dfs(start)
    return order


def main() -> None:
    graph = {
        0: [(1, 1), (2, 1)],
        1: [(3, 1)],
        2: [(3, 1)],
        3: []
    }
    order = dfs(graph, 0)
    print("DFS order starting from 0:", order)


if __name__ == "__main__":
    main()
