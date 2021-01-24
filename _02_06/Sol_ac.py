# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head != None:
            lis = [head.val]
            node = head
            while node.next != None:
                node = node.next
                lis.append(node.val)
            for i in range(-1, - len(lis) // 2 - 1, -1):
                if head.val != lis[i]:
                    return False
                head = head.next
        return True