# -*- encoding: utf-8 -*-
'''
@File    :   71. 简化路径.py
@Time    :   2020/04/22 10:38:12
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def simplifyPath(self, path: str) -> str:
        itmes=path.split('/')
        stack=[]
        for item in itmes:
            if item=='.':
                pass
            elif item=='..':
                if len(stack)>0:
                    stack.pop()
            elif item=='':
                pass
            else:
                stack.append(item)
        return '/'+'/'.join(stack)
if __name__ == "__main__":
    x=Solution()
    print(x.simplifyPath("/a/../../b/../c//.//"))