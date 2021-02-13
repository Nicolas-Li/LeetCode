class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        exist = [False] * (len(nums) + 1)
        for i in nums:
            exist[i] = True
        for j in range(1, len(exist)):
            if not exist[j]:
                yield j