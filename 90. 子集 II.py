# -*- encoding: utf-8 -*-
'''
@File    :   90. 子集 II.py
@Time    :   2020/04/23 10:53:50
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import copy


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums == None:
            return []
        nums.sort()
        res = []

        def bfs(i, tempnum):
            res.append(copy.deepcopy(tempnum))
            for j in range(i, len(nums)):
                if i == j or nums[j] != nums[j-1]:
                    bfs(j+1, tempnum+[nums[j]])
        bfs(0, [])
        return res


if __name__ == "__main__":
    x = Solution()
    print(x.subsetsWithDup([1, 2, 2,3]))
