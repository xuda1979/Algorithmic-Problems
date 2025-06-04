def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


def main():
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(quick_sort(arr))


if __name__ == '__main__':
    main()
