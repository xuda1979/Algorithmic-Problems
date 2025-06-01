import random
from typing import List


def quick_select(arr: List[int], k: int) -> int:
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


def main() -> None:
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"{k}rd smallest element is {quick_select(arr, k)}")


if __name__ == "__main__":
    main()
