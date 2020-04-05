# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    num=0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root :
            self.convertBST(root.right)
            root.val+=self.num
            self.num=root.val
            self.convertBST(root.left)
            return root
        return None