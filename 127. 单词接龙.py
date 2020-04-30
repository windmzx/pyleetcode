# -*- encoding: utf-8 -*-
'''
@File    :   127. 单词接龙.py
@Time    :   2020/04/30 09:17:40
@Author  :   windmzx
@Version :   1.0
@Desc    :   For leetcode template
'''

# here put the import lib
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        queue = [(beginWord, 1)]
        depth = 1
        visted = {}
        visted[beginWord] = 1
        wordList = set(wordList)
        while queue:
            newqueue = []
            depth += 1
            for word, de in queue:
                if word == endWord:
                    return de
                for i in range(len(word)):
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        nextword = word[:i]+char+word[i+1:]
                        if nextword in wordList:
                            if visted.get(nextword) and visted.get(nextword) < depth:
                                continue
                            newqueue.append((nextword, depth))
                            visted[nextword]=depth
            queue = newqueue
        return 0


if __name__ == "__main__":
    x = Solution()
    print(x.ladderLength(
        "ymain",
        "oecij",
        ["ymann", "yycrj", "oecij", "ymcnj", "yzcrj", "yycij",
            "xecij", "yecij", "ymanj", "yzcnj", "ymain"]
    ))
