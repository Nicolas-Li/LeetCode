class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

# 方法三：快慢指针
# 思路

# 避免使用 O(n)O(n) 额外空间的方法就是改变输入。

# 我们可以将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。比较完成后我们应该将链表恢复原样。虽然不需要恢复也能通过测试用例，但是使用该函数的人通常不希望链表结构被更改。

# 该方法虽然可以将空间复杂度降到 O(1)O(1)，但是在并发环境下，该方法也有缺点。在并发环境下，函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执行过程中链表会被修改。

# 算法

# 整个流程可以分为以下五个步骤：

# 找到前半部分链表的尾节点。
# 反转后半部分链表。
# 判断是否回文。
# 恢复链表。
# 返回结果。
# 执行步骤一，我们可以计算链表节点的数量，然后遍历链表找到前半部分的尾节点。

# 我们也可以使用快慢指针在一次遍历中找到：慢指针一次走一步，快指针一次走两步，快慢指针同时出发。当快指针移动到链表的末尾时，慢指针恰好到链表的中间。通过慢指针将链表分为两部分。

# 若链表有奇数个节点，则中间的节点应该看作是前半部分。

# 步骤二可以使用「206. 反转链表」问题中的解决方法来反转链表的后半部分。

# 步骤三比较两个部分的值，当后半部分到达末尾则比较完成，可以忽略计数情况中的中间节点。

# 步骤四与步骤二使用的函数相同，再反转一次恢复链表本身。

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci/solution/hui-wen-lian-biao-by-leetcode-solution-6cp3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。