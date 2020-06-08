# -*- encoding: utf-8 -*-
'''
@File    :   面试题12. 矩阵中的路径.py
@Time    :   2020/06/07 14:44:02
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == '#' or board[i][j]!=word[index]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            res = dfs(i+1, j, index+1) or dfs(i-1, j, index +
                                              1) or dfs(i, j+1, index+1) or dfs(i, j-1, index+1)
            board[i][j] = temp
            return res
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    if dfs(i, j, 0):
                        return True
        return False


if __name__ == "__main__":
    x = Solution()
    print(x.exist(

        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCDE"
    ))
