# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.left = [] # < 0
        self.right = [] # >= 0    

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root == None: return []
        
        import queue
        q = queue.Queue()
        q.put((root, 0, 0))
        while not q.empty():
            node = q.get()
            if node[0].left is not None:
                q.put((node[0].left, node[1] - 1, node[2] - 1))    
            if node[0].right is not None:
                q.put((node[0].right, node[1] + 1, node[2] - 1))       
            idx, arr = (node[1], self.right) if node[1] >= 0 else (-node[1] - 1, self.left)
            while True:
                try:
                    arr[idx]
                except IndexError:
                    arr.append([])
                else:
                    break
            arr[idx].append((node[0].val, node[1], node[2]))

        result = self.left.copy()
        result.reverse()
        result.extend(self.right)        
        for nodes in result:
            nodes.sort(key=lambda node: node[1] * 10000 * 10000 - node[2] * 10000 + node[0])
        result = list(map(lambda nodes: [node[0] for node in nodes], result))
        return result
