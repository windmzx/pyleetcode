# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res=""
        def helper(root,res):
            if root is None:
                res=res+"# "
                return res
            else:
                res+=str(root.val)+" "
            res=helper(root.left,res)
            res=helper(root.right,res)
            return res
        res=helper(root,res)

        return res

    def deserialize(self, data):
        from collections import deque

        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node=deque(data.split(" "))
        def helper(node ):
            val=node.popleft()
            if val!="#":
                root=TreeNode(int(val))
                root.left=helper(node)
                root.right=helper(node)
            else:
                root=None
                
            return root
        return helper(node)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == "__main__":
    x=Codec()
    root=TreeNode(3)
    root.left=TreeNode(1)
    root.left.left=None
    root.left.right=None
    root.right=TreeNode(5)
    root.right.left=TreeNode(8)
    root.right.right=TreeNode(9)
    res=x.serialize(root)
    print(res)
    res=x.deserialize(res)
    print(res)