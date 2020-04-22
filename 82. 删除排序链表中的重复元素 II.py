# -*- encoding: utf-8 -*-
'''
@File    :   82. 删除排序链表中的重复元素 II.py
@Time    :   2020/04/22 19:05:04
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        tval=float("nan")
        tnum=1
        res=ListNode(0)
        p=res
        cur=head
        while cur:
            if cur.val!=tval:
                if tnum==1:
                    p.next=cur
                    p=p.next
                tval=cur.val
                tnum=1
            else:
                tnum+=1
        p.next=None
        return res.next


if __name__ == "__main__":
    x=Solution()
    print()