class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)
        col=len(matrix[0])
        left=0
        up=0
        right=col-1
        down=row-1
        res=[]
        while left<=right:
            for i in range(left,right+1):
                res.append(matrix[up][i])
            up+=1
            if up>down:
                break
            for i in range(up,down+1):
                res.append(matrix[i][right])
            right-=1
            if right<left:
                break

            for i in range(right,left-1,-1):
                res.append(matrix[down][i])
            down-=1
            if down>up:
                break

            for i in range(down,up-1,-1):
                res.append(matrix[i][left])
            left+=1
            if left>right:
                break


        return res