from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        n=len(obstacleGrid[0])
        dp=[1]+[0]*n
        j=0
        for j in range(0,len(obstacleGrid)):
            for i in range(0,n):
                if obstacleGrid[j][i]==1:
                    dp[i]=0
                else:
                    dp[i]=dp[i]+dp[i-1]
            print(dp)
        return dp[-2]
# 这个非常巧妙的利了python的-1 这样我们可以将左边的边界放在最右边
if __name__ == "__main__":
    x=Solution()
    # print(x.uniquePathsWithObstacles([[0,1],[0,0]]))
    print(x.uniquePathsWithObstacles([[0,1,0],[0,1,0],[0,0,0]]))