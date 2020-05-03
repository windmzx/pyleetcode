# -*- encoding: utf-8 -*-
'''
@File    :   147. 对链表进行插入排序.py
@Time    :   2020/05/03 16:51:38
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
from untils.until import ListNode,stringToListNode
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        tail=newHead=ListNode(float("-inf"))
        cur=head
        
        while cur:
            temp=cur.next
            per=newHead
            while per.next and per.next.val <cur.val:
                per=per.next
            next=per.next
            per.next=cur
            cur.next=next

            cur=temp
        return newHead.next


        
if __name__ == "__main__":
    x=Solution()
    head=stringToListNode("[4,2,4,1]")
    res=x.insertionSortList(head)
    print()