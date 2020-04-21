# -*- encoding: utf-8 -*-
'''
@File    :   57. 插入区间.py
@Time    :   2020/04/21 18:13:45
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        i=0
        size=len(intervals)
        while i<size and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1

        while i<size and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        res.append(newInterval)

        while i<size :
            res.append(intervals[i])
            i+=1
        return res



if __name__ == "__main__":
    x = Solution()
    print(x.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
