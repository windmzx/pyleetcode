# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def ismirror(p:TreeNode,q:TreeNode)->bool:
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val == q.val:
                return ismirror(p.left,q.right) and ismirror(p.right,q.left)
            return False
        return ismirror(root.left,root.right)

if __name__ == "__main__":
    x=Solution()
    r1=TreeNode(1)
    r1.left=None
    r1.right=None


    print(x.isSymmetric(r1))