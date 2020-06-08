# -*- encoding: utf-8 -*-
'''
@File    :   面试题67. 把字符串转换成整数.py
@Time    :   2020/06/07 20:31:41
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None or str=='' or str=="-" or str=="+":
            return 0
        i=0
        res=0
        flag=False
        ll=len(str)
        while i<ll and str[i]==' ':
            i+=1
        if i>=ll:
            return 0
        if i<ll and str[i]!='-' and str[i]!="+" and (ord(str[i])< 48 or ord(str[i])>57):
            return 0
        if str[i]=="+" or str[i]=="-":
            if str[i]=='-':
                flag=True
            i+=1
        while i<ll and (ord(str[i])>= 48 and  ord(str[i])<=57):
                res=res*10+ord(str[i])-48
                i+=1
        if res> 1<<32:
            return -2147483648
        return res*-1 if flag else res
        
            

        
if __name__ == "__main__":
    x=Solution()
    print(x.strToInt("   -42"))