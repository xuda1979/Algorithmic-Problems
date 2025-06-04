def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for n in graph.get(start, []):
        if n not in visited:
            depth_first_search(graph, n, visited)
    return visited


def main():
    graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
    print(depth_first_search(graph, 1))


if __name__ == '__main__':
    main()
