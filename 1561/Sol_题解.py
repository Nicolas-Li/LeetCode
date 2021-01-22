class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        return sum(piles[n // 3 :: 2])

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-number-of-coins-you-can-get/solution/ni-ke-yi-huo-de-de-zui-da-ying-bi-shu-mu-by-leetco/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。