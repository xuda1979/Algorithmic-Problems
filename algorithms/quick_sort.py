from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def main() -> None:
    arr = [5, 8, 2, 9, 1]
    print(f"Original: {arr}")
    print(f"Sorted:   {quick_sort(arr)}")


if __name__ == "__main__":
    main()
