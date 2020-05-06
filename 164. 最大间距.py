# -*- encoding: utf-8 -*-
'''
@File    :   164. 最大间距.py
@Time    :   2020/05/06 16:03:39
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import math


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        n = len(nums)
        if n < 2:
            return 0
        minn = float('inf')
        maxn = float('-inf')

        for num in nums:
            minn = min(minn, num)
            maxn = max(maxn, num)
        size = math.ceil((maxn-minn)/(n-1))
        minbox = [float("inf") for i in range(n-1)]
        maxbox = [-1 for i in range(n-1)]

        for num in nums:
            index = (num-minn)//size
            if num == minn or num == maxn:
                continue
            minbox[index] = min(minbox[index], num)
            maxbox[index] = max(maxbox[index], num)
        maxGap = 0
        premax = minn
        for i in range(n-1):
            if maxbox[i] == -1:
                continue
            maxGap = max(maxGap, minbox[i]-premax)
            premax = maxbox[i]
        maxGap=max(maxGap,maxn-premax)
        return maxGap


if __name__ == "__main__":
    x = Solution()
    print(x.maximumGap([100, 3, 2, 1]))
