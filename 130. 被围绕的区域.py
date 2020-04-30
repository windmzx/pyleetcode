# -*- encoding: utf-8 -*-
'''
@File    :   130. 被围绕的区域.py
@Time    :   2020/04/30 10:31:27
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None:
            return
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        visted = [[0 for _ in range(n)] for _ in range(m)]

        def bfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] == 'O'and visted[i][j] != 1:
                visted[i][j] = 1
                bfs(i+1, j)
                bfs(i-1, j)
                bfs(i, j+1)
                bfs(i, j-1)
        for i in range(m):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][n-1] == "O":
                bfs(i, n-1)
        for j in range(n):
            if board[0][j] == "O":
                bfs(0, j)
            if board[m-1][j] == "O":
                bfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if visted[i][j] == 1:
                    board[i][j] = "O"


if __name__ == "__main__":
    x = Solution()
    borad = [["X", "X", "X", "X"], ["X", "O", "O", "X"], [
        "X", "O", "O", "X"], ["X", "O", "X", "X"]]
    x.solve(borad)
    print(borad)
