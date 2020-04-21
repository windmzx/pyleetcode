from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check(row, col):
            com = board[row][col]
            for i in range(row//3*3, row//3*3+3):
                for j in range(col//3*3, col//3*3+3):
                    if i == row and j == col:
                        continue
                    if board[i][j] != '.' and board[i][j] == com:
                        return False

            # for j in range(-row,0):
            #     if row+j<0 or row+j>=9 or col+j<0 or col+j>=9:
            #         pass
            #     else:
            #         if board[row+j][col+j]!='.' and board[row+j][col+j]==com:
            #             return False
            # for j in range(1,9-row):
            #     if row+j<0 or row+j>=9 or col+j<0 or col+j>=9:
            #         pass
            #     else:
            #         if board[row+j][col+j]!='.' and board[row+j][col+j]==com:
            #             return False
            # for j in range(-row,0):
            #     if row+j<0 or row+j>=9 or col-j<0 or col-j>=9:
            #         pass
            #     else:
            #         if board[row+j][col+j]!='.' and board[row+j][col-j]==com:
            #             return False
            # for j in range(1,9-row):
            #     if row+j<0 or row+j>=9 or col-j<0 or col-j>=9:
            #         pass
            #     else:
            #         if board[row+j][col+j]!='.' and board[row+j][col-j]==com:
            #             return False
            for j in range(0,9):
                if j==col:continue
                if board[row][j]!='.' and board[row][j]==com:
                    return False

            for j in range(0, 9):
                if j == row:
                    continue
                if board[j][col] != '.' and board[j][col] == com:
                    return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if not check(i, j):
                        return False
        return True


if __name__ == "__main__":
    x = Solution()
    print(x.isValidSudoku(
        [
            ["7", ".", ".", ".", "4", ".", ".", ".", "."],
            [".", ".", ".", "8", "6", "5", ".", ".", "."],
            [".", "1", ".", "2", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "9", ".", ".", "."],
            [".", ".", ".", ".", "5", ".", "5", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]

    ))
