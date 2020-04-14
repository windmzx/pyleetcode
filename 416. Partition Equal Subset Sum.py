from typing import List
import time
from functools import wraps

def timefn(fn):
    """计算性能的修饰器"""
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1: .5f} s")
        return result
    return measure_time

class Solution:
    @timefn
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        
        if summ%2==1:
            return False

        # nums.sort(reverse=True)
        target=summ//2

        dp=[0]*(target+1)
        dp[0]=1
        print(target)
        for num in nums:
            for j in range(target,num-1,-1):
                if dp[j-num]==1:
                    dp[j]=1
        return dp[target]==1
        
if __name__ == "__main__":
    x=Solution()
    print(x.canPartition([1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7,1,1,1,2,3,5,7]))
        