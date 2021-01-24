class Solution:
    def rotatedDigits(self, N: int) -> int:
        def isGood(n):
            badNums = {3, 4, 7}
            betterNums = {2, 5, 6, 9}
            nums = set(int(c) for c in str(n))
            if len(badNums & nums) == 0 and len(betterNums & nums) > 0:
                return True
            return False
        ans = 0
        for i in range(1, N+1):
            if isGood(i):
                ans += 1
        return ans
