# -*- encoding: utf-8 -*-
'''
@File    :   67. 二进制求和.py
@Time    :   2020/04/22 09:25:01
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena=len(a)
        lenb=len(b)
        ll=max(lena,lenb)
        buwei=['0']*abs(lena-lenb)
        if lena>lenb:
            b=''.join(buwei)+b
        elif lenb>lena:
            a=''.join(buwei)+a


        jinwei='0'
        re=['0']*ll
        for i in range(1,ll+1):
            temp=ord(a[-i])+ord(b[-i])+ord(jinwei)-144
            re[-i]=str(temp%2)
            jinwei=str(temp//2)
        if jinwei=='1':
            re=['1']+re
        return ''.join(re)
if __name__ == "__main__":
    x=Solution()
    print(x.addBinary("1010","1011"))