# -*- encoding: utf-8 -*-
'''
@File    :   61. 旋转链表.py
@Time    :   2020/04/21 19:10:32
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k < 1 or head == None:
            return head
        p1 = head
        step = 1
        while p1.next != None:
            p1 = p1.next
            step += 1
        if step == k or step == 1 or k % step == 0:
            return head

        tail = p1
        k = step-k % step-1
        tail.next = head

        p1 = head
        p2 = p1.next
        while k > 0:
            p1 = p1.next
            p2 = p2.next
            k -= 1
        # p2是新的头 p1是前指针
        p1.next = None

        tail.next = head
        return p2


if __name__ == "__main__":
    root = ListNode(1)
    # root.next=ListNode(2)
    # root.next.next=ListNode(3)
    # root.next.next.next=ListNode(4)
    # root.next.next.next.next=ListNode(5)
    x = Solution()
    res = x.rotateRight(root, 99)
    p = res
    while p != None:
        print(p)
        p = p.next
