class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([(i, nums[i]) for i in range(len(nums))], key=lambda num: num[1])
        left = 0
        right = len(nums) - 1
        while right > left:
            tmp = nums[left][1] + nums[right][1]
            if tmp == target:
                return [nums[left][0], nums[right][0]]
            elif tmp > target:
                right -= 1
            else:
                left += 1