# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            def check(node, floor, ceiling):
                if not node:
                    return True
                if not floor < node.val or not node.val < ceiling:
                    return False
                else:
                    return check(node.right, node.val, ceiling ) and check(node.left, floor, node.val)
            return check(root.left, float("-inf"), root.val) and check(root.right, root.val, float("inf"))
            