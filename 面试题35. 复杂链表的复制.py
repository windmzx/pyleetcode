# -*- encoding: utf-8 -*-
'''
@File    :   面试题35. 复杂链表的复制.py
@Time    :   2020/06/08 14:24:39
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        newhead = Node(0)
        tail = newhead
        while head:
            newnode = dic.get(head)
            if newnode is None:
                newnode = Node(head.val)
                dic[head] = newnode

            radomnode = dic.get(head.random)
            if radomnode is None:
                radomnode = Node(head.random.val)
                dic[head.random] = radomnode
            newnode.random = radomnode
            tail.next = newnode
            tail = tail.next
            head = head.next


if __name__ == "__main__":
    x = Solution()
    print()
