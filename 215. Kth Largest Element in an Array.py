from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums)<k:
            return 0
        maxnum=[0]*k
        head=0
        tail=0
        
        flag=True
        for i in range(0,len(nums)):
            if nums[i]<maxnum[head]:
                pass
            elif nums[i]>maxnum[tail%k]:
               
               
                else:
                    maxnum[head]=nums[i]
                    head=(head+1)%k 
                    tail=(tail+1)%k
            elif nums[i]<maxnum[tail]:
                p=head
                
                while nums[i]>maxnum[(p+1)%k]:
                    maxnum[p%k]=maxnum[(p+1)%k]
                    p=p+1
                maxnum[p%k]=nums[i]
        return maxnum[tail%k]
if __name__ == "__main__":
    x=Solution()
    re=x.findKthLargest([2,1],2)
    print(re)


