# -*- encoding: utf-8 -*-
'''
@File    :   140. 单词拆分 II.py
@Time    :   2020/05/03 14:29:58
@Author  :   windmzx 
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List
import copy
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result=[]
        maxlen=float('-inf')
        minlen=float('inf')
        for word in wordDict:
            ll=len(word)
            maxlen=max(maxlen,ll)
            minlen=min(minlen,ll)

        wordDict=set(wordDict)
        dic={}

        def backtrace(s:str):           
            if s=="":
                return [""]            
            if s in dic:
                return dic[s]
            res=[]
            for i in range(minlen,maxlen+1):
                if i<= len(s) and s[:i] in wordDict:
                    word=s[:i]
                    next=backtrace(s[i:])
                    for i in next:
                        res.append(word+" "+i)
            dic[s]=res
            return res
        result=backtrace(s)
        return result
if __name__ == "__main__":
    x=Solution()
    print(x.wordBreak("catsanddog",
["cat","cats","and","sand","dog"]))