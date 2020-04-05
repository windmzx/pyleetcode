# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            if root is None:
                return 0
            leftlen = helper(root.left)
            rightlen = helper(root.right)
            self.res = max(self.res, leftlen+rightlen+1)
            return max(leftlen, rightlen)+1

        helper(root)
        return self.res-1
if __name__ == "__main__":
    x=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    # root.left.left=TreeNode(4)
    # root.left.right=TreeNode(5)
    print(x.diameterOfBinaryTree(root))