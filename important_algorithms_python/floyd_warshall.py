def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def main():
    inf = 10**9
    matrix = [[0, 3, inf], [inf, 0, 1], [2, inf, 0]]
    for row in floyd_warshall(matrix):
        print(row)


if __name__ == '__main__':
    main()
