from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def main() -> None:
    arr = [4, 2, 7, 1, 3]
    print(f"Original: {arr}")
    print(f"Sorted:   {selection_sort(arr)}")


if __name__ == "__main__":
    main()
