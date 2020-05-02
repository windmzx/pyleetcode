# -*- encoding: utf-8 -*-
'''
@File    :   131. 分割回文串.py
@Time    :   2020/05/02 10:20:35
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.res = []
        self.helper(s, [])
        return self.res

    def helper(self, s, temp):
        if s == '':
            self.res.append(temp[:])
        for j in range(1, len(s)+1):
            if self.isvaild(s[:j]):
                temp.append(s[:j])
                self.helper(s[j:], temp)
                temp.pop()
    def isvaild(self, s):
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    x = Solution()
    print(x.partition("abba"))
