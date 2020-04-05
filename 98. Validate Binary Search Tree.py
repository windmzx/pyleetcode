# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, uper, lower):
            if root is None:
                return True
            val = root.val
            if val >= uper:
                return False
            if val <= lower:
                return False

            return helper(root.left, val, lower) and helper(root.right, uper, val)
        return helper(root, float('inf'), float('-inf'))


if __name__ == "__main__":
    x = Solution()
    root = TreeNode(0)
    root.left = None
    root.right = TreeNode(-1)
    print(x.isValidBST(root))
