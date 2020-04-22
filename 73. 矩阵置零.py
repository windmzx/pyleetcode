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
        row0=False
        col0=False
        for i in range(m):
            if matrix[i][0]==0:
                col0=True
        for i in range(n):
            if matrix[0][i]==0:
                row0=True

        for i in range(1,m):
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

        if(row0):
            for i in range(n):
                matrix[0][i]=0
        if(col0):
            for i in range(m):
                matrix[i][0]=0
        print(matrix)
if __name__ == "__main__":
    x=Solution()
    x.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]
)