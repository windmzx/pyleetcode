class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        return self.dfs(root, sum)+pathSum(root.right, sum)+pathSum(root.left, sum)

    def dfs(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        sum -= root.val
        if sum == 0:
            return 1+self.dfs(root.left, sum)+self.dfs(root.right, sum)
        else:
            return 0 + self.dfs(root.left, sum)+self.dfs(root.right, sum)
