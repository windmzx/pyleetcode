# -*- encoding: utf-8 -*-
'''
@File    :   面试题57 - II. 和为s的连续正数序列.py
@Time    :   2020/05/09 10:14:52
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:

        left = 0
        right = 1
        sum = 1
        res = []
        while left <= right:
            if sum == target:
                res.append([i for i in range(left, right+1)])
                right+=1
                sum+=right
            elif target > sum:

                right += 1
                sum += right
            elif target < sum:
                sum -= left
                left += 1
        return res


if __name__ == "__main__":
    x = Solution()
    print(x.findContinuousSequence(1))
