from typing import List
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if envelopes is None :
            return 0
        ll=len(envelopes)
        if ll==1:
            return 1
        envelopes.sort(key=lambda x:[x[0],-x[1]])
        newenv=[i[1]for i in envelopes]
        
        def find(dp,x):
            left=0
            right=len(dp)-1

            while left<=right:
                mid=(left+right)//2
                if dp[mid]==x:
                    return mid 
                if dp[mid]>x:
                    right=mid-1
                elif dp[mid]<x:
                    left=mid+1
            return left

        dp=[]
        dp.append(newenv[0])
        for i in range(1,ll):
            if newenv[i]>dp[-1]:
                dp.append(newenv[i])
            else:
                x= find(dp,newenv[i])
                dp[x]=newenv[i]
        return len(dp)



if __name__ == "__main__":
    li=[[1,2],[1,3],[2,3],[2,2]]
    x=Solution()
    res=x.maxEnvelopes(li)
    print(res)
