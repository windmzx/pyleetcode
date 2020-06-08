# -*- encoding: utf-8 -*-
'''
@File    :   递增数组找右边界.py
@Time    :   2020/06/08 22:04:20
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


def solution(array: List[int], target):
    mid = binarySearch(array, 0, len(array)-1, target)
    while mid+1 < len(array) and array[mid] == target:
        mid = binarySearch(array, mid+1, len(array), target)
    return array[mid]

def binarySearch(array, left, right, target):
    while left < right:
        mid = (left+right)//2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            right = mid-1
        else:
            left = mid
    return left


if __name__ == "__main__":
    print(solution([1,2,3,3,3,3,3,4],3))
