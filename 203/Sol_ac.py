# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return head
        pre = head
        nex = head.next
        while nex is not None:
            if nex.val == val:
                nex = nex.next
                pre.next = nex    
            else:
                pre = nex
                nex = nex.next     
        return head