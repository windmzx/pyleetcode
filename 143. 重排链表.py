# -*- encoding: utf-8 -*-
'''
@File    :   143. 重排链表.py
@Time    :   2020/05/02 16:09:10
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''
from untils.until import ListNode, stringToListNode
# here put the import lib
from typing import List
# Definition for singly-linked list.


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        back = slow.next
        slow.next = None

        back = self.reverse(back)

        newhead = ListNode(0)
        tail = newhead
        while head and back:
            tail.next = head
            head = head.next

            tail = tail.next
            tail.next = back
            back = back.next
            tail = tail.next
        return newhead.next

    def reverse(self, head: ListNode):
        pre = head
        cur = pre.next
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head.next = None
        return pre


if __name__ == "__main__":
    x = Solution()
    head = stringToListNode("[1, 2, 3, 4]")
    print(x.reorderList(head))
