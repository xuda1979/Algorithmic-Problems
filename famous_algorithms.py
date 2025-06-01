# Collection of classic algorithm implementations in Python.
# Each function demonstrates a standard algorithm for reference and teaching.

from collections import defaultdict, deque
import heapq
import math
import random

# 1. Binary Search

def binary_search(arr, target):
    """Return index of target in sorted arr or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 2. Bubble Sort

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# 3. Insertion Sort

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# 4. Selection Sort

def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# 5. Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 6. Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 7. Heap Sort

def heap_sort(arr):
    a = arr[:]
    heapq.heapify(a)
    return [heapq.heappop(a) for _ in range(len(a))]

# Graph algorithms assume graph is given as adjacency list: {node: [(neighbor, weight), ...]}

# 8. Breadth-First Search

def bfs(graph, start):
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

# 9. Depth-First Search

def dfs(graph, start):
    visited = set()
    order = []
    def _dfs(v):
        visited.add(v)
        order.append(v)
        for u, _ in graph.get(v, []):
            if u not in visited:
                _dfs(u)
    _dfs(start)
    return order

# 10. Dijkstra's Shortest Path

def dijkstra(graph, start):
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, w in graph.get(v, []):
            nd = d + w
            if nd < dist[u]:
                dist[u] = nd
                heapq.heappush(pq, (nd, u))
    return dict(dist)

# 11. Bellman-Ford Algorithm

def bellman_ford(graph, start):
    # graph is dict of {node: [(neighbor, weight), ...]}
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    vertices = list(graph.keys())
    for _ in range(len(vertices) - 1):
        for v in vertices:
            for u, w in graph.get(v, []):
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
    # Check for negative cycles
    for v in vertices:
        for u, w in graph.get(v, []):
            if dist[v] + w < dist[u]:
                return None  # Negative cycle detected
    return dict(dist)

# 12. Floyd-Warshall Algorithm

def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# 13. Prim's Minimum Spanning Tree

def prim_mst(graph, start=0):
    visited = set([start])
    edges = []
    pq = []
    for u, w in graph.get(start, []):
        heapq.heappush(pq, (w, start, u))
    mst = []
    while pq:
        w, v, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        mst.append((v, u, w))
        for nxt, wt in graph.get(u, []):
            if nxt not in visited:
                heapq.heappush(pq, (wt, u, nxt))
    return mst

# 14. Kruskal's Minimum Spanning Tree

def kruskal_mst(vertices, edges):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    def union(u, v):
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        if rank[ru] < rank[rv]:
            parent[ru] = rv
        elif rank[ru] > rank[rv]:
            parent[rv] = ru
        else:
            parent[rv] = ru
            rank[ru] += 1
        return True

    mst = []
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if union(u, v):
            mst.append((u, v, w))
    return mst

# 15. Topological Sort (Kahn's algorithm)

def topological_sort(graph):
    indeg = defaultdict(int)
    for v in graph:
        for u, _ in graph[v]:
            indeg[u] += 1
    queue = deque([v for v in graph if indeg[v] == 0])
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for u, _ in graph.get(v, []):
            indeg[u] -= 1
            if indeg[u] == 0:
                queue.append(u)
    if len(order) != len(graph):
        raise ValueError("Graph has a cycle")
    return order

# 16. Knuth-Morris-Pratt (KMP) pattern search

def kmp_search(text, pattern):
    if not pattern:
        return 0
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                return i - j + 1
    return -1

# 17. Longest Common Subsequence (LCS)

def longest_common_subsequence(a, b):
    m, n = len(a), len(b)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + a[i]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], key=len)
    return dp[m][n]

# 18. Quick Select (k-th smallest)

def quick_select(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k out of range")
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    if k <= len(lows):
        return quick_select(lows, k)
    if k <= len(lows) + len(pivots):
        return pivot
    return quick_select(highs, k - len(lows) - len(pivots))

# 19. Tarjan's Strongly Connected Components

def tarjan_scc(graph):
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    on_stack = set()
    sccs = []

    def strongconnect(v):
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

# 20. Kosaraju's Strongly Connected Components

def kosaraju_scc(graph):
    visited = set()
    order = []

    def dfs1(v):
        visited.add(v)
        for u, _ in graph.get(v, []):
            if u not in visited:
                dfs1(u)
        order.append(v)

    def dfs2(v, component, gr):
        component.append(v)
        visited.add(v)
        for u, _ in gr.get(v, []):
            if u not in visited:
                dfs2(u, component, gr)

    for v in graph:
        if v not in visited:
            dfs1(v)
    gr = defaultdict(list)
    for v in graph:
        for u, w in graph[v]:
            gr[u].append((v, w))
    visited.clear()
    sccs = []
    for v in reversed(order):
        if v not in visited:
            comp = []
            dfs2(v, comp, gr)
            sccs.append(comp)
    return sccs

# 21. A* Search

def a_star_search(graph, start, goal, heuristic):
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

if __name__ == "__main__":
    # Simple usage demonstration
    arr = [5, 2, 9, 1, 5, 6]
    print("quick_sort:", quick_sort(arr))
    print("binary_search 5:", binary_search(sorted(arr), 5))
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print("dijkstra:", dijkstra(graph, 0))

