class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci/solution/hui-wen-lian-biao-by-leetcode-solution-6cp3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。