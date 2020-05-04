# -*- encoding: utf-8 -*-
'''
@File    :   151. 翻转字符串里的单词.py
@Time    :   2020/05/04 15:25:27
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        s = list(s)
        s=self.cleanspace(s)
        ll=len(s)
        self.reverse(s, i, ll-1)
        i = 0
        j = 0
        while j < ll:
            while j < ll and s[j] != ' ':
                j += 1
            self.reverse(s, i, j-1)
            i = j+1
            j = i
        return "".join(s)

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def cleanspace(self,s):
        n = len(s)
        i = 0
        j = 0
        while j < n:
            while j <n and s[j] == ' ':
                j += 1
            while j < n and s[j] != ' ':
                s[i] = s[j]
                i += 1
                j += 1
            while j <n and s[j] == ' ':
                j += 1
            if j < n:
                s[i] = " "
                i += 1

        return s[:i]
if __name__ == "__main__":
    x = Solution()
    # print(x.cleanspace(list("  hello  wor d  ")))
    print(x.reverseWords(" hello   word!  "))
