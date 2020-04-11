from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp=nums[0]
        count=1
        for i in nums[1:]:
            if i==temp:
                count+=1
            else:
                count-=1
                if count==0:
                    count=1
                    temp=i
        return temp
if __name__ == "__main__":
    x=Solution()
    print(x.majorityElement([1,1,2,2,1]))
