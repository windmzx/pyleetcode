class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n<1:
            return 0
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=10
        temp=9
        for i in range(2,n+1):            
            temp*=(11-i)
            print(temp)
            dp[i]=dp[i-1]+temp
            print(dp)
        return dp[-1]
if __name__ == "__main__":
    x=Solution()
    print(x.countNumbersWithUniqueDigits(7))