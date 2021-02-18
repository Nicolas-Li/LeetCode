class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        q = collections.deque()
        res = 0
        for i in range(len(A)):
            if len(q) > 0 and q[0] + K <= i:
                q.popleft()
            if len(q) % 2 == A[i]:
                if i + K > len(A): return -1
                q.append(i)
                res += 1
        return res