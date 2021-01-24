class Solution(object):
    def rotatedDigits(self, N):
        A = map(int, str(N))

        memo = {}
        def dp(i, equality_flag, involution_flag):
            if i == len(A): return +(involution_flag)
            if (i, equality_flag, involution_flag) not in memo:
                ans = 0
                for d in xrange(A[i] + 1 if equality_flag else 10):
                    if d in {3, 4, 7}: continue
                    ans += dp(i+1, equality_flag and d == A[i],
                              involution_flag or d in {2, 5, 6, 9})
                memo[i, equality_flag, involution_flag] = ans
            return memo[i, equality_flag, involution_flag]

        return dp(0, True, False)

# 思路

# 根据好数定义，每个好数只能包含数字 0125689，并且至少包含 2569 中的一个。因此可以逐个写出小于等于 N 的所有好数。

# 这道题目可以使用动态规划解答。状态可以表示为三个变量 i, equality_flag, involution_flag。其中 i 表示当前正在写第 i 位数字；equality_flag 表示已经写出的 j 位数字是否等于 N 的 j 位前缀；involution_flag 表示从最高位到比当前位高一位的这段前缀中是否含有 2569 中的任意一个数字。

# dp(i, equality_flag, involution_flag) 表示在特定 equality_flag，involution_flag 的状态下，有多少种从 i 到末尾的后缀能组成一个好数。最终的结果为 dp(0, True, False)。

# 注：数字 N 从最高位到最低位的索引，从 0 开始，并依次增大。第 i 位表示索引为 i 的位置。

# 算法

# 如果 equality_flag 为 true，表示第 i 位能取到的最大数字为 N 的第 i 位对应的数字。并且还需要根据当前状态决定可以写哪些数字。

# 在代码实现中，我们分别使用了自顶向下的方法和自底向上的方式。Python 代码实现的是自顶向下的方法，从 for d in xrange(...) 到 memo[...] = ans 这四行代码清晰的说明了状态之间的递归关系。

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/rotated-digits/solution/xuan-zhuan-shu-zi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
