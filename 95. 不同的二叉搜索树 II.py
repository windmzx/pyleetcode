# -*- encoding: utf-8 -*-
'''
@File    :   95. 不同的二叉搜索树 II.py
@Time    :   2020/04/24 09:52:59
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(nodes: List[int]) -> TreeNode:
            res=[]
            if len(nodes)==0:
                return [None]
            for i in range(len(nodes)):
                lefts=helper(nodes[0:i])
                rights=helper(nodes[i+1:])
                for left in lefts:
                    for right in rights:
                        root=TreeNode(nodes[i])
                        root.left=left
                        root.right=right
                        res.append(root)
            return res
        source=[i+1 for i in range(n)]
        return helper(source)

if __name__ == "__main__":
    x = Solution()
    trees=x.generateTrees(3)
    for tree in trees:
        print(tree)
