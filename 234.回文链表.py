# -*- encoding: utf-8 -*-
'''
@File    :   234.回文链表.py
@Time    :   2020/06/07 14:29:46
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
from untils.until import stringToListNode,ListNode
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return False
        p1=head
        p2=head
        while p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
        cur=p1
        pre=cur.next

        while pre :
            temp=pre.next
            pre.next=cur
            cur=pre
            pre=temp
        p1.next=None
        while cur and head:
            if cur.val!=head.val:
                return False
            cur=cur.next
            head=head.next
        return True

if __name__ == "__main__":
    x=Solution()
    head=stringToListNode("[1,2,3,3,2,1]")
    print(x.isPalindrome(head))