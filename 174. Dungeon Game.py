class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])

        dp=[0]*n+[1]
        
        for i in range(n-1,0-1,-1):
            dp[i]=max(dp[i+1]-dungeon[m-1][i],1)
        for i in range(m-2,0-1,-1):
            for j in range(n-1,0-1,-1):
            #    print(" "+str(i)+" "+str(j))
                if(j==n-1):
                    dp[j]=max(1,dp[j]-dungeon[i][j])
                else:
                    dp[j]=max(1,min(dp[j+1]-dungeon[i][j],dp[j]-dungeon[i][j]) )
        return(dp[0])