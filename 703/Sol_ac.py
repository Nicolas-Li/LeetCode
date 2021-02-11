class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
        if self.k - len(self.nums) == 1:
            self.nums.append(-10001)

    def ins(self, begin, end, obj):
        if end == begin:
            self.nums.insert(begin, obj)
            self.nums.pop(-2)
        elif end - begin == 1:
            if obj >= self.nums[begin]:
                self.nums.insert(begin, obj)
            else:
                self.nums.insert(end, obj)
            self.nums.pop()
        else:
            mid = (end + begin) // 2
            if obj > self.nums[mid]:
                self.ins(begin, mid, obj)
            elif obj < self.nums[mid]:
                self.ins(mid, end, obj)
            else:
                self.nums.insert(mid, obj)
                self.nums.pop()


    def add(self, val: int) -> int:
        if val > self.nums[self.k-1]:
            self.ins(0, self.k, val)
        return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)