class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        # 并查集
        class UnionFind:
            def __init__(self, n: int):
                self.parent = list(range(n))
                self.size = [1] * n
                self.setCount = n
            def findSet(self, x: int):
                if self.parent[x] == x:
                    return x
                self.parent[x] = self.findSet(self.parent[x])
                return self.parent[x]
            def unite(self, x, y):
                x, y = self.findSet(x), self.findSet(y)
                if x == y:
                    return False
                if self.size[x] < self.size[y]:
                    x, y = y, x
                self.parent[y] = x
                self.size[x] += self.size[y]
                self.setCount -= 1
                return True
        unionFindSet = UnionFind(n)
        for x, y in connections:
            unionFindSet.unite(x, y)
        return unionFindSet.setCount - 1
        