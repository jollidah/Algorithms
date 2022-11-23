from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l = 0
        q = Queue()
        if not root:
            return 0
        q.put([root, 1])
        while not q.empty():
            node, l = q.get()
            if node.left != None:
                q.put([node.left, l + 1])
            if node.right != None:
                q.put([node.right, l + 1])
        return l

# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
