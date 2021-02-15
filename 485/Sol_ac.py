class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        ans = 0
        ret = 0
        for i in nums:
            if ans == ans + i:
                ret = max(ret, ans)
                ans = 0
            else:
                ans += 1
        return ret