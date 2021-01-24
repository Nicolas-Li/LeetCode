class Solution(object):
    def kSimilarity(self, A, B):
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in xrange(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/k-similar-strings/solution/xiang-si-du-wei-k-de-zi-fu-chuan-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
