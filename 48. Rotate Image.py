from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)

        n=len(matrix[0])

        x1=0
        while x1<(m-1)/2:
            x2=0
            while x2<m/2:
                temp=matrix[m-1-x2][0+x1]            
                matrix[m-1-x2][0+x1]=matrix[m-1-x1][m-1-x2]
                matrix[m-1-x1][m-1-x2]=matrix[0+x2][m-1-x1]
                matrix[0+x2][m-1-x1]=matrix[0+x1][0+x2]
                matrix[0+x1][0+x2]=temp
                x2+=1
            print(matrix)
            x1+=1
            
if __name__ == "__main__":
    x=Solution()
    m=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    m2=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    m3=[
        [1,2],
        [3,4]
    ]
    x.rotate(m2)
