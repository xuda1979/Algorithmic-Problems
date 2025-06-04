import bisect

def longest_increasing_subsequence(arr):
    lis = []
    for x in arr:
        pos = bisect.bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)
        else:
            lis[pos] = x
    return len(lis)


def main():
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(longest_increasing_subsequence(arr))


if __name__ == '__main__':
    main()
