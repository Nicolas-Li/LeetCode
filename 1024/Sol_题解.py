# 思路及解法

# 注意到对于所有左端点相同的子区间，其右端点越远越有利。且最佳方案中不可能出现两个左端点相同的子区间。于是我们预处理所有的子区间，对于每一个位置 ii，我们记录以其为左端点的子区间中最远的右端点，记为 \textit{maxn}[i]maxn[i]。

# 我们可以参考「55. 跳跃游戏的官方题解」，使用贪心解决这道题。

# 具体地，我们枚举每一个位置，假设当枚举到位置 ii 时，记左端点不大于 ii 的所有子区间的最远右端点为 \textit{last}last。这样 \textit{last}last 就代表了当前能覆盖到的最远的右端点。

# 每次我们枚举到一个新位置，我们都用 \textit{maxn}[i]maxn[i] 来更新 \textit{last}last。如果更新后 \textit{last} == ilast==i，那么说明下一个位置无法被覆盖，我们无法完成目标。

# 同时我们还需要记录上一个被使用的子区间的结束位置为 \textit{pre}pre，每次我们越过一个被使用的子区间，就说明我们要启用一个新子区间，这个新子区间的结束位置即为当前的 \textit{last}last。也就是说，每次我们遇到 i == \textit{pre}i==pre，则说明我们用完了一个被使用的子区间。这种情况下我们让答案加 11，并更新 \textit{pre}pre 即可。

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/video-stitching/solution/shi-pin-pin-jie-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        maxn = [0] * T
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)
        
        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last
        
        return ret
