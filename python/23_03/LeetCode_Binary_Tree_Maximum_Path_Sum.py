# Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxV = -1e9
        self.maxN = -1e9

    def dfs(self, p) -> int:
        if p.val <= 0:
            self.maxN = max(self.maxN, p.val)
        if p.left == None:
            if p.right != None:
                m = max(self.dfs(p.right) + p.val, 0)
                self.maxV = max(self.maxV, m)
                return m
            else:
                m = max(p.val, 0)
                self.maxV = max(self.maxV, m)
                return m
        else:
            if p.right == None:
                m = max(self.dfs(p.left) + p.val, 0)
                self.maxV = max(self.maxV, m)
                return m
            else:
                l = max(self.dfs(p.left), 0)
                r = max(self.dfs(p.right), 0)
                m = max(l + p.val, r + p.val, 0)
                self.maxV = max(self.maxV, m, l + r + p.val)
                return m

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxN if self.maxV == 0 else self.maxV

# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
