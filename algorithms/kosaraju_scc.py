from collections import defaultdict
from typing import Dict, List, Tuple


def kosaraju_scc(graph: Dict[int, List[Tuple[int, int]]]) -> List[List[int]]:
    visited = set()
    order: List[int] = []

    def dfs1(v: int) -> None:
        visited.add(v)
        for u, _ in graph.get(v, []):
            if u not in visited:
                dfs1(u)
        order.append(v)

    def dfs2(v: int, component: List[int], gr: Dict[int, List[Tuple[int, int]]]) -> None:
        component.append(v)
        visited.add(v)
        for u, _ in gr.get(v, []):
            if u not in visited:
                dfs2(u, component, gr)

    for v in graph:
        if v not in visited:
            dfs1(v)
    gr: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    for v in graph:
        for u, w in graph[v]:
            gr[u].append((v, w))
    visited.clear()
    sccs = []
    for v in reversed(order):
        if v not in visited:
            comp: List[int] = []
            dfs2(v, comp, gr)
            sccs.append(comp)
    return sccs


def main() -> None:
    graph = {
        0: [(1, 1)],
        1: [(2, 1)],
        2: [(0, 1), (3, 1)],
        3: [(4, 1)],
        4: []
    }
    print("Kosaraju SCCs:", kosaraju_scc(graph))


if __name__ == "__main__":
    main()
