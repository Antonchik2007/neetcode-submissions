# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            if abs(left-right) > 1:
                return float("inf")
            return 1 + max(left, right)
        if maxDepth(root) == float("inf"):
            return False
        else:
            return True