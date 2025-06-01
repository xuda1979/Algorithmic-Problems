from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def main() -> None:
    arr = [9, 1, 7, 3, 2]
    print(f"Original: {arr}")
    print(f"Sorted:   {insertion_sort(arr)}")


if __name__ == "__main__":
    main()
