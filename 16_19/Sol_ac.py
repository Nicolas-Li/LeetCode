class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        m = len(land)
        n = len(land[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(i, j):
            size = 0
            if 0 <= i < m and 0 <= j < n:
                if land[i][j] == 0 and (not visited[i][j]):
                    visited[i][j] = True
                    size += 1
                    for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        size += dfs(i + di, j + dj)
            return size
        sizes = []
        for i in range(m):
            for j in range(n):
                pond_size = dfs(i, j)
                if pond_size != 0:
                    sizes.append(pond_size)
        return sorted(sizes)