# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        import sys
        self.ans = -sys.maxsize

    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        node_max = max(left + node.val, node.val, node.val + right)
        self.ans = max(left + node.val + right, node_max, self.ans)
        return node_max

    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans