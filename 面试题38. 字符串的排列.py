# -*- encoding: utf-8 -*-
'''
@File    :   面试题38. 字符串的排列.py
@Time    :   2020/05/09 10:00:24
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        s=list(s)
        s.sort()
        s="".join(s)
        def helper(s1, s2):
            if len(s2) == 1:
                res.append(s1+s2)
                return
            for i in range(len(s2)):
                if i!=0 and s2[i]==s2[i-1]:
                    continue
                else:
                    helper(s1+s2[i], s2[:i]+s2[i+1:])
        helper("",s)
        return res

if __name__ == "__main__":
    x = Solution()
    print(x.permutation("aab"))
