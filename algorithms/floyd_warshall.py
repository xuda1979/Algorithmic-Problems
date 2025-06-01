from typing import List


def floyd_warshall(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def main() -> None:
    INF = 99999
    matrix = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    for row in floyd_warshall(matrix):
        print(row)


if __name__ == "__main__":
    main()
