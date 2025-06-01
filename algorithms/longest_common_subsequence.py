from typing import List

def longest_common_subsequence(a: str, b: str) -> str:
    m, n = len(a), len(b)
    dp: List[List[str]] = [["" for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + a[i]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], key=len)
    return dp[m][n]


def main() -> None:
    a = "AGGTAB"
    b = "GXTXAYB"
    lcs = longest_common_subsequence(a, b)
    print(f'String A: {a}')
    print(f'String B: {b}')
    print(f'Longest Common Subsequence: {lcs}')


if __name__ == "__main__":
    main()
