class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        rangeK = collections.defaultdict(lambda: collections.defaultdict(int))
        rangeVisited = collections.defaultdict(lambda: collections.defaultdict(bool))
        all_digit = set()
        for i in range(len(A)):
            all_digit.add(A[i])
            rangeK[0][i+1] = len(all_digit)
        ret = 0
        def dfs(start, end):
            if not rangeVisited[start][end]:
                rangeVisited[start][end] = True
                if rangeK[start][end] == 0:
                    all_digit.clear()
                    for i in range(start, end):
                        all_digit.add(A[i])
                        rangeK[start][i+1] = len(all_digit)
                if rangeK[start][end] >= K:
                    nonlocal ret
                    if rangeK[start][end] == K: 
                        ret += 1
                    for mid in range(start+1, end):
                        if mid-start >= K: dfs(start, mid)
                        if end-mid >= K: dfs(mid, end)
        dfs(0, len(A))
        return ret