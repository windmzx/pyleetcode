# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:



        def helper(root):
            if root==None:
                return root
            if root.left==None:
                return root
            l=root.left
            r=root.right
            res=helper(l)
            l.left=r
            l.right=None
            return res
        return helper(root)