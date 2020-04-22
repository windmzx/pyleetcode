# -*- encoding: utf-8 -*-
'''
@File    :   77. 组合.py
@Time    :   2020/04/22 11:53:49
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import copy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        source=[]
        for i in range(n):
            source.append(i+1)
        res=[]
        def dfs(i,temp):
            if len(temp)==k:
                res.append(copy.deepcopy(temp))
                return
            for j in range(i,n):
                temp.append(source[j])
                dfs(j+1,temp)
                temp.pop()
        
        dfs(0,[])
        return res

    


if __name__ == "__main__":
    x=Solution()
    print(x.combine(4,2))