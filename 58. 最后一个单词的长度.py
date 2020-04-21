# -*- encoding: utf-8 -*-
'''
@File    :   58. 最后一个单词的长度.py
@Time    :   2020/04/21 18:56:53
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                length+=1
            elif length!=0:
                return length
        return  length
if __name__ == "__main__":
    x=Solution()
    print(x.lengthOfLastWord(" "))