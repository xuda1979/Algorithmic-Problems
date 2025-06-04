from collections import deque

def breadth_first_search(graph, start):
    visited = []
    queue = deque([start])
    seen = set([start])
    while queue:
        v = queue.popleft()
        visited.append(v)
        for n in graph.get(v, []):
            if n not in seen:
                seen.add(n)
                queue.append(n)
    return visited


def main():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    print(breadth_first_search(graph, 1))


if __name__ == '__main__':
    main()
