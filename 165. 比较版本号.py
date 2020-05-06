# -*- encoding: utf-8 -*-
'''
@File    :   165. 比较版本号.py
@Time    :   2020/05/06 17:26:22
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        len1 = len(ver1)
        len2 = len(ver2)
        num1=0
        num2=0
        l=max(len1,len2)
        for i in range(l):
            if i >= len1:
                num1 = 0
                num2 = int(ver2[i])
            elif i >= len2:
                num2 = 0
                num1 = int(ver1[i])
            else:
                num1 = int(ver1[i])
                num2 = int(ver2[i])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0

if __name__ == "__main__":
    x = Solution()
    print(x.compareVersion("1","1.1"))
