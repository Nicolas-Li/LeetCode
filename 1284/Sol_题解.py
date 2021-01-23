class Solution:
    def encode(self, mat, m, n):
        x = 0
        for i in range(m):
            for j in range(n):
                x = x * 2 + mat[i][j]
        return x

    def decode(self, x, m, n):
        mat = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mat[i][j] = x & 1
                x >>= 1
        return mat

    def convert(self, mat, m, n, i, j):
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            i0, j0 = i + di, j + dj
            if 0 <= i0 < m and 0 <= j0 < n:
                mat[i0][j0] ^= 1

    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        x_start, step = self.encode(mat, m, n), 0
        if x_start == 0:
            return step

        visited = {x_start}
        q = queue.Queue()
        q.put_nowait(x_start)

        while not q.empty():
            step += 1
            k = q.qsize()
            for _ in range(k):
                status = self.decode(q.get_nowait(), m, n)
                for i in range(m):
                    for j in range(n):
                        self.convert(status, m, n, i, j)
                        x_cur = self.encode(status, m, n)
                        if x_cur == 0:
                            return step
                        if x_cur not in visited:
                            visited.add(x_cur)
                            q.put_nowait(x_cur)
                        self.convert(status, m, n, i, j)

        return -1

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/solution/zhuan-hua-wei-quan-ling-ju-zhen-de-zui-shao-fan-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。