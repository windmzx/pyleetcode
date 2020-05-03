# -*- encoding: utf-8 -*-
'''
@File    :   145. 二叉树的后序遍历.py
@Time    :   2020/05/03 11:54:12
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
from untils.until import TreeNode,stringToTreeNode
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        stack=[]
        if root:
            stack.append(root)
        pre=None
        res=[]
        while len(stack)!=0:
            node=stack[-1]
            if( node.right==None and node.left==None) or (pre!=None and (pre==node.left or pre==node.right)):
                res.append(node.val)
                pre=node
                stack.pop()
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
if __name__ == "__main__":
    x=Solution()
    head=stringToTreeNode("[1,null,2,3]")
    print(x.postorderTraversal(head))