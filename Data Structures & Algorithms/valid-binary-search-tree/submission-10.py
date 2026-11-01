# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            
        def is_valid(node, lower_bound, upper_bound):
            if not node:
                return True
            if node.left and( not node.left.val < node.val or not node.left.val > lower_bound ):
                return False
            if node.right and( not node.right.val > node.val or not node.right.val < upper_bound ):
                return False
            return is_valid(node.left, lower_bound, node.val) and is_valid(node.right, node.val, upper_bound)
        return is_valid(root, float("-inf"), float("inf"))
            

        
            
            