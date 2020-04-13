# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def split(head):
            if head.next == None:
                return head
            p =head
            q=head
            while q != None and q.next  !=  None:
                temp=p
                p=p.next
                q=q.next.next
            temp.next = None

            l=split(head)
            r=split(p)
            return merge(l,r)

        def merge(l1,l2):
            head=ListNode(-1)
            cur=head
            while l1!=None and l2!=None:
                if l1.val<l2.val:
                    cur.next=l1
                    l1=l1.next
                    cur=cur.next
                else:
                    cur.next=l2
                    l2=l2.next
                    cur=cur.next
                if l1!=None:
                    cur.next=l1
                if l2!=None:
                    cur.next=l2
            return head.next
        if head is None:
            return None
        return split(head)
if __name__ == "__main__":
    x=Solution()
    li=ListNode(3)
    p=li
    p.next=ListNode(1)
    p=p.next
    p.next=ListNode(4)
    p=p.next
    p.next=ListNode(0)
    p=p.next
    p.next=ListNode(2)
    p=p.next
    p.next=ListNode(5)
    p=p.next
    re=x.sortList(li)
    while re!=None:
        print(re.val)
        re=re.next