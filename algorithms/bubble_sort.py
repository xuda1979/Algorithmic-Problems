from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def main() -> None:
    arr = [5, 1, 4, 2, 8]
    print(f"Original: {arr}")
    print(f"Sorted:   {bubble_sort(arr)}")


if __name__ == "__main__":
    main()
