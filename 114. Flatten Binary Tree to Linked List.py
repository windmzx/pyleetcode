class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 

        temp=root.right

        self.flatten(root.left)
        self.flatten(temp)

        root.right=root.left
        root.left=None

        while root.right!=None:
            root=root.right
        root.right=temp