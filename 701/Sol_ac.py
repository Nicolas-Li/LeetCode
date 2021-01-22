# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val, None, None)
        if val > root.val:
            if root.right is None:
                root.right = TreeNode(val, None, None)
            else:
                self.insertIntoBST(root.right, val)
        elif val < root.val:
            if root.left is None:
                root.left = TreeNode(val, None, None)
            else:
                self.insertIntoBST(root.left, val)
        return root