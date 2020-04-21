# -*- encoding: utf-8 -*-
'''
@File    :   66. 加一.py
@Time    :   2020/04/21 20:16:35
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=len(digits)
        if l<1:
            l=1
            digits=[0]
        jinwei=0
        digits[-1]+=1
        for i in range(l-1,-1,-1):
            temp=digits[i]+jinwei
            digits[i]=temp%10
            jinwei=temp//10
        if jinwei!=0:
            return[jinwei]+digits
        return digits   
if __name__ == "__main__":
    x=Solution()
    print()