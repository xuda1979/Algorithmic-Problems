from typing import List


def binary_search(arr: List[int], target: int) -> int:
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


def main() -> None:
    arr = [1, 3, 5, 7, 9, 11]
    target = 7
    print(f"Array: {arr}")
    print(f"Searching for {target}: index {binary_search(arr, target)}")


if __name__ == "__main__":
    main()
