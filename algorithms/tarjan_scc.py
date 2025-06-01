from typing import Dict, List, Tuple

def tarjan_scc(graph: Dict[int, List[Tuple[int, int]]]) -> List[List[int]]:
    index = 0
    stack: List[int] = []
    indices = {}
    lowlink = {}
    on_stack = set()
    sccs: List[List[int]] = []

    def strongconnect(v: int) -> None:
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        for w, _ in graph.get(v, []):
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            component = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.append(w)
                if w == v:
                    break
            sccs.append(component)

    for v in graph:
        if v not in indices:
            strongconnect(v)
    return sccs


def main() -> None:
    graph = {
        0: [(1, 1)],
        1: [(2, 1)],
        2: [(0, 1), (3, 1)],
        3: [(4, 1)],
        4: []
    }
    sccs = tarjan_scc(graph)
    print("Tarjan SCCs:", sccs)


if __name__ == "__main__":
    main()
