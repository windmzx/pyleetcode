# -*- encoding: utf-8 -*-
'''
@File    :   面试题13. 机器人的运动范围.py
@Time    :   2020/05/09 11:20:29
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[0 for _ in range(n)]for _ in range(m)]
        res=[0]
        def dfs(i, j):
            if i < 0 or i > m or j < 0 or j > n or (i % 10+i//10+j % 10+j//10) > k or visited[i][j]:
                return
            visited[i][j] = 1
            res[0]+=1
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i-1, j-1)

        dfs(0,0)
        return res[0]
if __name__ == "__main__":
    x = Solution()
    print(x.movingCount(2, 3, 1))
