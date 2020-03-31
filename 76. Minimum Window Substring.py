class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        # 构建两个数组 来保存字符串中字符数量
        dics=[0]*128
        dict=[0]*128
        for i in range(len(t)):
            dict[i]+=1
        start,end=0, len(t) 
        while(end<len(s)):

