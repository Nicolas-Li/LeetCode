class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if (len(nums)) == 0: return -1
        center = 0
        left_sum = 0
        right_sum = sum(nums[center+1:])
        while center < len(nums):
            if left_sum == right_sum:
                return center
            else:
                if center == len(nums) - 1:
                    return -1
                left_sum += nums[center]
                center += 1
                right_sum -= nums[center]
            