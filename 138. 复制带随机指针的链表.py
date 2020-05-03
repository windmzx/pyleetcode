# -*- encoding: utf-8 -*-
'''
@File    :   138. 复制带随机指针的链表.py
@Time    :   2020/05/03 10:32:13
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        dic={}
        newhead=tail=Node(0)
        cur = head
        while cur:
            if cur not in dic:
                dic[cur]=Node(cur.val)
            tail.next=dic[cur]
            tail=tail.next
            rad=cur.random
            if rad is None:
                pass
            else:
                if rad not in dic:
                    dic[rad]=Node(rad.val)
                dic[cur].random=dic[rad]
            cur=cur.next  
        return newhead.next              

if __name__ == "__main__":
    head=Node(7)
    head.random=None
    head.next=Node(13)
    head.next.random=head
    x=Solution()
    print(x.copyRandomList(head))