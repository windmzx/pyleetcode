# -*- encoding: utf-8 -*-
'''
@File    :   面试题05. 替换空格.py
@Time    :   2020/05/18 15:19:01
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

class Solution:
    def replaceSpace(self, s: str) -> str:
        tmp=0
        ll=len(s)-1
        for i in range(len(s)):
            if s[i]==' ':
                tmp+=1
        s=list(s)+['' for i in range(2*tmp)]
        i=len(s)-1
        while i>ll and ll>=0:
            if s[ll]!=' ':
                s[i]=s[ll]
                i-=1
                ll-=1
            else:
                s[i]='0'
                s[i-1]='2'
                s[i-2]='%'
                i-=3
                ll-=1
        return "".join(s)

if __name__ == "__main__":
    x=Solution()
    print(x.replaceSpace(" "))