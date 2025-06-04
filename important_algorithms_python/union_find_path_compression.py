class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def main():
    uf = UnionFind(3)
    uf.union(0, 1)
    print(uf.find(0), uf.find(1))


if __name__ == '__main__':
    main()
