# -*- encoding: utf-8 -*-
'''
@File    :   129. 求根到叶子节点数字之和.py
@Time    :   2020/04/30 09:45:05
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

from untils.until import TreeNode
from untils.until import stringToTreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = [0]
        
        def helper(root, num):
            if root.left is None and root.right is None:
                res[0] += num*10+root.val
                return
            if root.left:
                helper(root.left, num*10+root.val)
            if root.right:
                helper(root.right, num*10+root.val)
        if root is None:
            return 0
        helper(root, 0)
        return res[0]


if __name__ == "__main__":
    x = Solution()
    head = stringToTreeNode("[1,2,3]")
    print(x.sumNumbers(head))
