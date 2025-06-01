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
    INF = 10**9
    matrix = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]
    result = floyd_warshall(matrix)
    print("Floyd-Warshall distance matrix:")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
