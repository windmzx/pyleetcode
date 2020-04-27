# -*- encoding: utf-8 -*-
'''
@File    :   107. 二叉树的层次遍历 II.py
@Time    :   2020/04/27 14:56:21
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
# Definition for a binary tree node.
import copy
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q = queue.Queue()
        q.put(root)
        res = []
        while q.qsize()!=0:
            size = q.qsize()
            temp = []
            while size > 0:
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                size -= 1
                temp.append(node.val)
            res.insert(0, copy.deepcopy(temp))
        return res


if __name__ == "__main__":
    x = Solution()
    root = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(5)

    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    print(x.levelOrderBottom(root))
