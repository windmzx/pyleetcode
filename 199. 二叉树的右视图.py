# -*- encoding: utf-8 -*-
'''
@File    :   199. 二叉树的右视图.py
@Time    :   2020/04/22 10:05:50
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:          
        if root is None:
            return []
        q=queue.Queue()
        q.put(root)
        res=[]
        while(not q.empty()):
            size=q.qsize()
            while size>0:
                node=q.get()
                val=node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                size-=1
            res.append(val)
        return res
           
if __name__ == "__main__":
    x=Solution()
    root=TreeNode(1)
    root.right=TreeNode(3)
    root.right.right=TreeNode(4)
    print(x.rightSideView(root))