from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        res=[]
        p=root
        while p or stack:
            while p :
                stack.append(p)
                p=p.left
            p=stack.pop()
            print(p.val)
            res.append(p.val)
            p=p.right
        return res
if __name__ == "__main__":
    x=Solution()
    root = TreeNode(0)
    root.left = None
    root.right = TreeNode(-1)
    x.inorderTraversal(root)
            