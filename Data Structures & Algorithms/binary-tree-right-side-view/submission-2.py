# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = collections.deque()
        q.append(root)
        result = []

        while q:
            qLen = len(q)
            node = None
            for i in range(qLen):
                n =  q.popleft()
                if n is not None:
                    node = n
                    q.append(n.left)
                    q.append(n.right)


            if node is not None:
                result.append(node.val)      

        return result  