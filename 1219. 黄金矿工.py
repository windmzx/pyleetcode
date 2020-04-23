# -*- encoding: utf-8 -*-
'''
@File    :   1219. 黄金矿工.py
@Time    :   2020/04/22 21:01:56
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if grid==None:
            return 0
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        if n==0:
            return 0
        res=0


        def dfs(i,j,cursum):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return cursum
            temp=grid[i][j]
            grid[i][j]=0
            a=dfs(i+1,j,cursum+temp)
            b=dfs(i-1,j,cursum+temp)
            c=dfs(i,j+1,cursum+temp)
            d=dfs(i,j-1,cursum+temp)
            grid[i][j]=temp
            return max(max(a,b),max(c,d))
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    res=max(res,dfs(i,j,0))
        return res
   

if __name__ == "__main__":
    x=Solution()
    print(x.getMaximumGold(
      [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    ))