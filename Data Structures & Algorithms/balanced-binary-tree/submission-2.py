# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def dfs(node):
            if node is None:
                return (0, True)
            
            v1 = dfs(node.left)
            v2 = dfs(node.right)

            return (1+max(v1[0], v2[0]), abs(v1[0]- v2[0]) <=1 and v1[1] and v2[1])

        return dfs(root)[1]