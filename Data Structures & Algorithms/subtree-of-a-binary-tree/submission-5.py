# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(n1, n2):
            if n1 is None and n2 is None:
                return True
            elif n1 is None or n2 is None:
                return False
            
            res = (n1.val == n2.val)

            return res and sameTree(n1.left, n2.left) and sameTree(n2.right, n1.right)

        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False
            
            res = sameTree(node1, node2)
            if res == True:
                return True
            
            return dfs(node1.left, node2) or dfs(node1.right, node2)

        return dfs(root, subRoot)

            



        