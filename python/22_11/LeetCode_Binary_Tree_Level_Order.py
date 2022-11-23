from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:    # 입력이 빈 리스트일 경우 예외처리
            return res
        level = -1      # 층이 달라지는지 확인하기 위해서 만든 변수
        q = Queue()     # BFS를 활용하여 문제 해결
        q.put([root, 0])
        while not q.empty():
            node, l = q.get()
            if level != l:
                res.append([])
                level += 1
            res[l].append(node.val)
            if node.left != None:
                q.put([node.left, l + 1])
            if node.right != None:
                q.put([node.right, l + 1])
        print(res)
        return res
      
# https://leetcode.com/problems/binary-tree-level-order-traversal/
