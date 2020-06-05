# -*- encoding: utf-8 -*-
'''
@File    :   bigK.py
@Time    :   2020/06/04 19:14:32
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import random


class Solution:
    def partion(self, left, right, array):
        pri = array[left]
        while left < right:

            while left < right and array[right] <= pri:
                right -= 1
            if left < right:
                array[left] = array[right]

            while left < right and array[left] >= pri:
                left += 1
            if left < right:
                array[right] = array[left]
        array[left] = pri
        return left

    def bigK(self,  left, right, array, k):
        res = self.partion(left, right, array)
        if res > k:
            self.bigK(left, res-1, array, k)
        elif k > res:
            self.bigK(res+1, right, array, k)


if __name__ == "__main__":
    x = Solution()
    array = [random.randint(1, 1000) for i in range(100)]
    x.bigK(0, len(array)-1, array, 10)
    print(array)
