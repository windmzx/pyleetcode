# -*- encoding: utf-8 -*-
'''
@File    :   99. 恢复二叉搜索树.py
@Time    :   2020/04/25 17:28:03
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        before = None
        first = None
        second = None
        cur = root
        while cur:
            if cur.left != None:
                per = cur.left
                while per.right and per.right != cur:
                    per = per.right
                if per.right == None:
                    per.right = cur
                    cur = cur.left
                    continue
                else:
                    per.right = None

            if first == None and before != None and before.val > cur.val:
                first = before
            if first != None and before != None and before.val > cur.val:
                second = cur
            before = cur
            cur = cur.right
        print(first.val)
        print(second  .val)
        first.val, second.val = second.val, first.val
        return("success")

if __name__ == "__main__":
    x = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.left = TreeNode(3)

    print(x.recoverTree(root))
 