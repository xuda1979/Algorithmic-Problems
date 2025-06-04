def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def main():
    arr = [5, 2, 9, 1, 5, 6]
    print(insertion_sort(arr))


if __name__ == '__main__':
    main()
