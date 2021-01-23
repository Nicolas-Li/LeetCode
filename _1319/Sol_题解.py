# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        uf = UnionFind(n)
        for x, y in connections:
            uf.unite(x, y)
        
        return uf.setCount - 1

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/solution/lian-tong-wang-luo-de-cao-zuo-ci-shu-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。