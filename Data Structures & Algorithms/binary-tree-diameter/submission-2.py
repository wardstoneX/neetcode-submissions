# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDiam = 0
        def dfs(node):
            nonlocal maxDiam
            if node is None:
                return 0

            v1 = dfs(node.left)
            v2 = dfs(node.right)

            maxDiam = max(maxDiam, v1+v2)
            return 1 + max(v1,v2) 
        
        dfs(root)
        return maxDiam