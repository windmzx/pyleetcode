class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        swap=root.left
        root.left=root.right
        root.right=swap

        invertTree(root.left)
        invertTree(root.right)

        return root