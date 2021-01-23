class Solution:
    def trait(self, mat: List[List[int]]) -> int:
        ret = 0
        k = 1
        for row in mat:
            for col in row:
                ret += col * k
                k *= 2
        return ret
    
    def flip(self, x: int, y: int, mat: List[List[int]]) -> List[List[int]]:
        filped = [row.copy() for row in mat]
        filped[x][y] ^= 1
        d = [-1, 1]
        m = len(filped)
        n = len(filped[0])
        for dxy in d:
            x_idx = x + dxy
            if 0 <= x_idx < m:
                filped[x_idx][y] ^= 1
            y_idx = y + dxy
            if 0 <= y_idx < n:
                filped[x][y_idx] ^= 1
        return filped

    def minFlips(self, mat: List[List[int]]) -> int:
        rel = [0] * 512
        m = len(mat)
        n = len(mat[0])
        std_trait = self.trait(mat)
        if std_trait == 0:
            return 0
        import queue
        q = queue.Queue()
        class WrappedMat:
            def __init__(self, mat: List[List[int]], trait: int, deep: int):
                self.mat = mat if mat else [[0] * n for _ in range(m)]
                self.trait = trait
                self.deep = deep
        q.put(WrappedMat(None, 0, 0))
        rel[0] = 1
        while not q.empty():
            wrappedMat = q.get()
            for i in range(m):
                for j in range(n):
                    fliped_mat = self.flip(i, j, wrappedMat.mat)
                    fliped_trait = self.trait(fliped_mat)              
                    if rel[fliped_trait] == 0:
                        if fliped_trait == std_trait:
                            return wrappedMat.deep + 1     
                        rel[fliped_trait] = 1
                        q.put(WrappedMat(fliped_mat, fliped_trait, wrappedMat.deep + 1))
        return -1

