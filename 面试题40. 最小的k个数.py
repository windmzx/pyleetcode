# -*- encoding: utf-8 -*-
'''
@File    :   面试题40. 最小的k个数.py
@Time    :   2020/05/09 10:41:59
@Author  :   windmzx
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def heap(k, n):
            left = k*2+1
            right = k*2+2
            if left < n and arr[k] < arr[left]:
                arr[k], arr[left] = arr[left], arr[k]
                heap(left, n)
            if right < n and arr[k] < arr[right]:
                arr[k], arr[right] = arr[right], arr[k]
                heap(right, n)
        for i in range(k//2, -1, -1):
            heap(i, k)
        for i in range(k, len(arr)):
            if arr[0] > arr[i]:
                arr[0] = arr[i]
                heap(0, k)
        return arr[0:k]


if __name__ == "__main__":
    x = Solution()
    print(x.getLeastNumbers([5, 1, 2, 23, 3, 5, 63, 2, 4], 5))
