import heapq

def heap_sort(arr):
    h = arr[:]
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]


def main():
    arr = [3, 1, 4, 1, 5, 9]
    print(heap_sort(arr))


if __name__ == '__main__':
    main()
