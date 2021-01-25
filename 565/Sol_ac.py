class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        max_nest = 0

        for i in range(n):
            rel = set()
            nex = i
            len_nest = 0
            while True:
                if not visited[nex]:
                    visited[nex] = True
                    len_nest += 1
                    nex = nums[nex]
                else:
                    break
            max_nest = max(max_nest, len_nest)
        
        return max_nest