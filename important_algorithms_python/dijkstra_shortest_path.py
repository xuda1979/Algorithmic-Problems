import heapq

def dijkstra_shortest_path(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def main():
    graph = {0: [(1, 2), (2, 4)], 1: [(2, 1)], 2: []}
    print(dijkstra_shortest_path(graph, 0))


if __name__ == '__main__':
    main()
