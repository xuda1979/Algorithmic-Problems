def knapsack_dynamic_programming(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]


def main():
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    print(knapsack_dynamic_programming(weights, values, capacity))


if __name__ == '__main__':
    main()
