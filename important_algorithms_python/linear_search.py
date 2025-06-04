def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1


def main():
    arr = [3, 1, 4, 2]
    print(linear_search(arr, 4))


if __name__ == '__main__':
    main()
