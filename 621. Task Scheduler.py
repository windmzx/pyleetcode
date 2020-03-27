# 这道题的关键点在于如果所需的时间大于任务数的时候，可能出现多个数量一样的最大数量任务，因此最后需要加N，而不是加1
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tnum=[]
        for s in set(tasks):
            tnum.append(tasks.count(s))
        maxnum=max(tnum)
        return max(
            (maxnum-1)*(n+1)+tnum.count(maxnum),
            len(tasks)
        )