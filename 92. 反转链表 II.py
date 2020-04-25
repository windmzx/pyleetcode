# -*- encoding: utf-8 -*-
'''
@File    :   92. 反转链表 II.py
@Time    :   2020/04/23 15:18:19
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None:
            return head
        # m==n 则不进行翻转 
        if m==n:
            return head
        newhead=ListNode(0)
        newhead.next=head
        p=newhead
        ll=n-m
        while m>1:
            p=p.next
            m-=1
        # p是前驱节点 p.next是开始翻转的节点
        i=0
        per=p
        cur=p.next
        while i<=ll:
            nextnode=cur.next
            cur.next=per
            per=cur
            cur=nextnode
            i+=1
        p.next.next=cur
        p.next=per
        return newhead.next        
if __name__ == "__main__":
    x=Solution()
    head=ListNode(2)
    head.next=ListNode(3)

    res=x.reverseBetween(head,1,2)

    while res:
        print(res.val)
        res=res.next