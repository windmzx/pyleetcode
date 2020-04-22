# -*- encoding: utf-8 -*-
'''
@File    :   1291. 顺次数.py
@Time    :   2020/04/22 20:31:35
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        ll = 0
        tlow = low
        head = 0
        while tlow > 0:
            ll += 1
            head = tlow % 10
            tlow = tlow//10
        l2=0
        thigh=high
        while thigh>0:
            l2+=1
            thigh=thigh//10
        res = []
        i = head

        while True:
            re = self.create(i, ll)
            if re > high:
                return res
            if re > low:
                res.append(re)
            i += 1
            if i == 10:
                i = 1
                ll += 1

    def create(self,first: int, length) -> int:
        res = ""
        cur = first
        i = 1
        while i <= length and cur <= 9:
            res += str(cur)
            i += 1
            cur += 1
        if len(res) < length:
            return -1
        else:
            return int(res)


if __name__ == "__main__":
    x = Solution()
    print(x.sequentialDigits(8881, 99999))
