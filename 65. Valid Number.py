class Solution:
    def isNumber(self, s: str) -> bool:
        def getaction(i:str):
            if i==' ':
                return 0
            if i=='+' or i=='-':
                return 1
            if ord(i)>=48 and ord(i)<=57:
                return 2
            if i=='.':
                return 3
            if i=='e':
                return 4
            return 5
        table = [
            [0, 1, 6, 2, -1, -1],
            [-1, -1, 6, 2, -1,-1],
            [-1, -1, 3, -1, -1, -1],
            [8, -1, 3, -1, 4, -1],
            [-1, 7, 5, -1, -1, -1],
            [8, -1, 5, -1, -1, -1],
            [8, -1, 6, 3, 4, -1],
            [-1, -1, 5, -1, -1, -1],
            [8, 8, -1, -1, -1, -1]
        ]

        state=0
        for i in s:
            action=getaction(i)
            if action==-1:
                return False
            state=table[state][action]
        if state==3 or state==5 or state==6 or state==8:
            return True
        return False

if __name__ == "__main__":
    x=Solution()
    print(x.isNumber("+Fe"))
