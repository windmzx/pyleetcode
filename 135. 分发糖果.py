# -*- encoding: utf-8 -*-
'''
@File    :   135. 分发糖果.py
@Time    :   2020/05/02 19:50:16
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ll = len(ratings)
        res = [1 for _ in range(ll)]

        for i in range(1, ll):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in range(ll-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)
        return sum(res)


if __name__ == "__main__":
    x = Solution()
    print(x.candy([1, 3, 4, 5, 2]))
