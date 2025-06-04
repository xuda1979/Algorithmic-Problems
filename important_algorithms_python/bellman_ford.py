def bellman_ford(vertices, edges, start):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


def main():
    vertices = [0, 1, 2]
    edges = [(0, 1, 2), (1, 2, 1), (0, 2, 4)]
    print(bellman_ford(vertices, edges, 0))


if __name__ == '__main__':
    main()
