from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix==None:
            return 
        m=len(matrix)
        if m<1:
            return
        n=len(matrix[0])
        for i in range(0,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(1,n):
                    matrix[i][j]=0
        for i  in range(1,n):
            if matrix[0][i]==0:
                for j in range(1,m):
                    matrix[j][i]=0
        print(matrix)
if __name__ == "__main__":
    x=Solution()
    x.setZeroes([
        [1,0,3],
        [4,5,6],
        [7,8,9]
    ])