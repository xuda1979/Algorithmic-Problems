from typing import List
import heapq


def heap_sort(arr: List[int]) -> List[int]:
    a = arr[:]
    heapq.heapify(a)
    return [heapq.heappop(a) for _ in range(len(a))]


def main() -> None:
    arr = [12, 11, 13, 5, 6, 7]
    print(f"Original: {arr}")
    print(f"Sorted:   {heap_sort(arr)}")


if __name__ == "__main__":
    main()
