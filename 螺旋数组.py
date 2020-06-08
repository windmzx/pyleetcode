# -*- encoding: utf-8 -*-
'''
@File    :   螺旋数组.py
@Time    :   2020/06/08 21:46:05
@Author  :   windmzx
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


def shuzu(m, n):
    left = 0
    right = n-1
    top = 0
    under = m-1

    array = [[0 for i in range(n)]for _ in range(m)]

    num = 1
    while num < m*n:
        for i in range(left, right+1):
            array[top][i] = num
            num += 1
        top += 1

        for i in range(top, under+1):
            array[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left-1, -1):
            array[under][i] = num
            num += 1
        under -= 1

        for i in range(under, top-1, -1):
            array[i][left] = num
            num += 1
        left += 1


        for line in array:
            print(line)
        print()


if __name__ == "__main__":
    shuzu(4,3)
