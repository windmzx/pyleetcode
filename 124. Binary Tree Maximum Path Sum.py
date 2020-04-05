# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res=[0]
        def helper(root,res):
            if root is None:
                return 0
            leftmax=max(0,helper(root.left,res))
            rightmax=max(0,helper(root.right,res))
            res[0]=max(res[0],(root.val+leftmax+rightmax))
            return root.val+max(leftmax,rightmax)
        helper(root,res)
        return res[0]
