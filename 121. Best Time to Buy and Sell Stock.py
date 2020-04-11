from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<1:
            return 0
        res=0
        minv=prices[0]

        for i in range(1,len(prices)):
            minv=min(minv,prices[i])
            res=max(res,prices[i]-minv)
            
        return res

if __name__ == "__main__":
    x=Solution()
    print(x.maxProfit([7,1,5,3,6,4]))