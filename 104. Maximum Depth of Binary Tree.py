class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def helper(n: int, root: TreeNode):
            if root is None:
                return n
            else:
                return max(helper(n, root.left), helper(n, root.right))+1
        return max(helper(0,root.left),helper(0,root.right))+1