class Solution:
    def __init__(self):
        self.found_c = []
        self.ans = 0
        self.bias = 0
    def kSimilarity(self, A: str, B: str) -> int:
        n = len(A)
        visited = [False] * n
        for i in range(n):
            if A[i] == B[i]:
                visited[i] = True
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                start_c = A[i]
                self.found_c = [start_c]
                def dfs(self, pos: int) -> int:
                    if B[pos] == start_c:
                        return 1
                    try:
                        idx = self.found_c.index(B[pos])
                        self.bias += 1
                        self.found_c = self.found_c[0:idx]
                    except ValueError:
                        pass
                    try:
                        nex = visited.index(False) - 1
                    except ValueError:
                        return 0
                    while True:
                        nex = A.find(B[pos], nex + 1)
                        if nex == -1:
                            return 0
                        if not visited[nex]:
                            visited[nex] = True
                            self.found_c.append(A[nex])
                            break
                    return dfs(self, nex) + 1
                self.ans += dfs(self, i) - 1
        return self.ans - self.bias
