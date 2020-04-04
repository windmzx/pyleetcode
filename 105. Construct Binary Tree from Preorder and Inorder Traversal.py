# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        v=preorder[0]
        root=TreeNode(v)
        i=0
        while inorder[i]!=v:
            i+=1
        root.left=self.buildTree(preorder[1:i+1],inorder[0:i])
        root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
        return root