# -*- encoding: utf-8 -*-
'''
@File    :   125. 验证回文串.py
@Time    :   2020/04/29 17:08:15
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1
        while i < j:
            if not self.isNumorChar(s[i]):
                i+=1
                continue
            if not self.isNumorChar(s[j]):
                j-=1
                continue
            if s[i]!=s[j]:
                return False
            i+=1

            j-=1
                
        return True
    def isNumorChar(self,i):
        numi=ord(i)
        return (numi >= 48 and numi <= 57) or(numi >= 97 and numi <= 122)


if __name__ == "__main__":
    x = Solution()
    print(x.isPalindrome("ab  a"))
