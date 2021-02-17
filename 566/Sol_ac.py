class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) == 0 or (r * c != len(nums) * len(nums[0])):
            return nums
        def get_ele():
            for row in nums:
                for i in row:
                    yield i
        ret = []
        row = list[int]()
        i = 0
        for ele in get_ele():
            i += 1
            row.append(ele)
            if i == c:
                ret.append(row)
                row = list[int]()
                i = 0
        return ret