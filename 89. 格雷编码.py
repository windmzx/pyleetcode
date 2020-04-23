# -*- encoding: utf-8 -*-
'''
@File    :   89. 格雷编码.py
@Time    :   2020/04/23 09:54:48
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import copy
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res=[0]
        add=1
        for i in range(n):
            ll=len(res)
            for j in range(ll):
                res.append(add+res[ll-j-1])
            add*=2
        
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.grayCode(3))