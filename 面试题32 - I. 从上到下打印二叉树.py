# -*- encoding: utf-8 -*-
'''
@File    :   面试题32 - I. 从上到下打印二叉树.py
@Time    :   2020/06/07 19:08:17
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        import queue
        if not root:
            return []
        q=queue.Queue()
        q.put(root)
        res=[]
        while q.qsize()!=0:
            l=q.qsize()
            for i in range(l):
                node=q.get()
                res.append(node.val)
                if node.left:q.put(node.left)
                if node.right:q.put(node.right)
        return res
                


if __name__ == "__main__":
    x=Solution()
    print()