# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # 第一个节点 包含根
        def dfs(root)->(int,int):
            if root is None:
                return 0,0
            a,b=dfs(root.left)
            c,d=dfs(root.right)
            r1=max(a,b)+max(c,d)
            r2=max(b,d)+root.val
            return r1,r2
        return max (dfs(root))

