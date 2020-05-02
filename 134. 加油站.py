# -*- encoding: utf-8 -*-
'''
@File    :   134. 加油站.py
@Time    :   2020/05/02 15:35:24
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        temp = [0 for _ in range(len(gas))]

        for i in range(len(gas)):
            temp[i] = gas[i]-cost[i]
        sumfu = 0
        sumzheng = 0
        fuindex = 0
        minnum = float('-inf')
        minindex = 0
        sumtemp = 0
        for i in range(len(temp)):
            sumtemp += temp[i]
            if minnum > sumtemp:
                minnum = sumtemp
                minindex = i
        if sum(temp) >= 0:
            return (fuindex+1) % len(gas)
        else:
            return -1


if __name__ == "__main__":
    x = Solution()
    print(x.canCompleteCircuit(
        [1, 2, 3, 4, 5],
        [3, 4, 5, 1, 2]
    ))
