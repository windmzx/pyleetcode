# -*- encoding: utf-8 -*-
'''
@File    :   133. 克隆图.py
@Time    :   2020/05/02 14:48:33
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        d = {}

        def dfs(old):
            if old not in d:
                d[old] = new = Node(old.val)
                new.neighbors = []
                for neiber in old.neighbors:
                    new.neighbors.append(dfs(neiber))

            return d[old]
        return dfs(node)


if __name__ == "__main__":
    x = Solution()
    print()
