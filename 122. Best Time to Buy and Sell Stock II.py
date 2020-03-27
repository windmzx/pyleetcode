from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                res+=prices[i]-prices[i-1]
        return res


if __name__ == "__main__":
    x = Solution()
    print(x.maxProfit([1,2,3]))