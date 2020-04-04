from typing import List
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        res=[]
        temp=[]
        q = queue.Queue()
        q.put(root)
        qlen=0
        while not q.empty():
            qlen=q.qsize()
            temp=[]
            while(qlen>0):
                t=q.get()
                temp.append(t)
                q.put(t.left)
                q.put(t.right)
                qlen-=1
            res.append(temp)

            
