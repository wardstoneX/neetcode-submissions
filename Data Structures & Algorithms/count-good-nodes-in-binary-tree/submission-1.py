# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def good(node, maxVal):
            if node is None:
                return 0
            result = 0
            if node.val >= maxVal:
                result +=1
            result += good(node.left, max(maxVal, node.val))  
            result += good(node.right, max(maxVal, node.val))  
            
            return result
        
        return good(root, root.val)
        