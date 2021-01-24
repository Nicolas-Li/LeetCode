class Solution(object):
    def kSimilarity(self, A, B):
        if A == B: return 0

        N = len(A)
        alphabet = 'abcdef'
        pairs = [(a, b) for a in alphabet for b in alphabet if a != b]
        index = {p: i for i, p in enumerate(pairs)}

        count = [0] * len(index)
        for a, b in itertools.izip(A, B):
            if a != b:
                count[index[a, b]] += 1

        seen = set()
        for size in xrange(2, len(alphabet) + 1):
            for cand in itertools.permutations(alphabet, size):
                i = cand.index(min(cand))
                seen.add(cand[i:] + cand[:i])

        possibles = []
        for cand in seen:
            row = [0] * len(alphabet) * (len(alphabet) - 1)
            for a, b in itertools.izip(cand, cand[1:] + cand[:1]):
                row[index[a, b]] += 1
            possibles.append(row)

        ZERO = tuple([0] * len(row))
        memo = {ZERO: 0}
        def solve(count):
            if count in memo: return memo[count]

            ans = float('-inf')
            for row in possibles:
                count2 = list(count)
                for i, x in enumerate(row):
                    if count2[i] >= x:
                        count2[i] -= x
                    else: break
                else:
                    ans = max(ans, 1 + solve(tuple(count2)))

            memo[count] = ans
            return ans

        return sum(count) - solve(tuple(count))

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/k-similar-strings/solution/xiang-si-du-wei-k-de-zi-fu-chuan-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
