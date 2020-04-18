# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res=0
        
        def helper(root,res):
            if root!=None:
                left=root.left
                right=root.right

                if left:
                    if left.left==None and left.right==None:
                        res+=left.val
                helper(left)
                helper(right)
        helper(root,res)
        return res