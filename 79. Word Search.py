from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])


        def helper(i, j, word):
            if len(word)==0:
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[0]:
                return False
            board[i][j]="#"
            if helper(i+1, j, word[1:]) or helper(i-1, j, word[1:]) or helper(i, j+1, word[1:]) or helper(i, j-1, word[1:]):
                return True
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if helper(i, j, word):
                        return True

        return False
if __name__ == "__main__":
    x=Solution()
    print(x.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
,"ABF"))