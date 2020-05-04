# -*- encoding: utf-8 -*-
'''
@File    :   150. 逆波兰表达式求值.py
@Time    :   2020/05/04 15:19:42
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token=="+":
                t2=stack.pop()
                t1=stack.pop()
                stack.append(t1+t2)
            elif token=="-":
                t2=stack.pop()
                t1=stack.pop()
                stack.append(t1-t2)
            elif token=="*":
                t2=stack.pop()
                t1=stack.pop()
                stack.append(t1*t2)
            elif token=="/":
                t2=stack.pop()
                t1=stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[-1]
if __name__ == "__main__":
    x=Solution()
    print(x.evalRPN(["2","1","+","3","*"]))