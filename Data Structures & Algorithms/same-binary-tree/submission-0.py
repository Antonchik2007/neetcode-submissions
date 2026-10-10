# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #check the first node and it's children -- the base case
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val != q.val:
            return False
        
        def checkSame(p, q):
            if not p and not q:

                return True
            if not p and q:
                return False
            if p and not q:
                return False
            if p.val != q.val:
                return False
            else:
                return checkSame(p.left, q.left) and checkSame(p.right, q.right)
                

            return True
        return checkSame(p, q)
        

        
        