class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[0]*len(grid[0])+[0]
        for i in range(len(grid[0])):
            dp[i]=dp[i-1]+grid[0][i]
        print(dp)
        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                if j==0:
                    dp[j]=dp[j]+grid[i][j]
                else:
                    dp[j]=min(grid[i][j]+dp[j-1],grid[i][j]+dp[j])
            print(dp)
        return dp[-2]