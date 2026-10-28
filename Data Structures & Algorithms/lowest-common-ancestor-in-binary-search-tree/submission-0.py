# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if p and q not on the same side, return the current node.
        #if we reached p or q, return itself
        if root == p:
            return p
        elif root == q:
            return q
        elif root.val < p.val and root.val > q.val or root.val > p.val and root.val < q.val:
            return root
        elif root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, q, p)
