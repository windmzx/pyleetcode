# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == q or root == p:
           return root
        r1=self.lowestCommonAncestor(root.left,p,q)
        r2=self.lowestCommonAncestor(root.right,p,q)
        if r1 and r2:
            return root 
        elif r1:
            return r1
        else:
            return r2
