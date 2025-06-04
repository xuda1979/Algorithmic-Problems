import heapq

def prim_mst(graph, start):
    visited = set([start])
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)
    mst = []
    while edges:
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            for nxt, w2 in graph[v]:
                if nxt not in visited:
                    heapq.heappush(edges, (w2, v, nxt))
    return mst


def main():
    graph = {1: [(2, 1), (4, 2)], 2: [(1, 1), (3, 2)], 3: [(2, 2), (4, 1)], 4: [(1, 2), (3, 1)]}
    print(prim_mst(graph, 1))


if __name__ == '__main__':
    main()
