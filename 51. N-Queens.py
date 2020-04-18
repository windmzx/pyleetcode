from typing import List
from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [['.' for _ in range(n)] for _ in range(n)]
        result=[]

        def helper(line,res):
            for i in range(n):
                if check(line,i):
                    if line==n-1:
                        res[line][i]='Q'
                        result.append(deepcopy(res))
                        res[line][i]='.'
                    else:
                        res[line][i]="Q"
                        helper(line+1,res)
                        res[line][i]='.'


        def check(row,col):
            for i in range(n):
                if res[i][col]=="Q":
                    return False
            for j in range(n):
                if res[row][j]=="Q":
                    return False
            for i in range(-row,n-row):
                if col+i <n and col+i>=0:
                    if res[row+i][col+i]=="Q":
                        return False
                if col-i <n and col-i>=0:
                    if res[row+i][col-i]=="Q":
                        return False
            return True
        helper(0,res)
        for i in range(len(result)):
            for j in range(n):
                result[i][j]=''.join(result[i][j])
        return result
if __name__ == "__main__":
    x=Solution()
    res=x.solveNQueens(4)
    for i in res:
        for j in i:

            print(j)