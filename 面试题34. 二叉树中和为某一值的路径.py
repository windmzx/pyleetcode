# -*- encoding: utf-8 -*-
'''
@File    :   面试题34. 二叉树中和为某一值的路径.py
@Time    :   2020/06/08 12:30:37
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
from untils.until import TreeNode, stringToTreeNode
import copy


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        if not root:
            return []

        def help(head, ssum, path):
            print(ssum)
            if ssum == sum:
                res.append(copy.deepcopy(path))
            if head.left:
                help(head.left, ssum+head.left.val, path+[head.left.val])
            if head.right:
                help(head.right, ssum+head.right.val, path+[head.right.val])
        help(root, root.val, [root.val])
        return res


if __name__ == "__main__":
    x = Solution()
    print(x.pathSum(
        stringToTreeNode(
            "[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]"), 22
    ))
