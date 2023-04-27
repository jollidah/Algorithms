def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

    stack = [(root, False)]
    ans = []
    while stack:
        curr, visited = stack.pop()
        if curr:
            if visited:
                ans.append(curr.val)
            else:
                stack.append((curr, True))
                stack.append((curr.right, False))
                stack.append((curr.left, False))


    return ans
