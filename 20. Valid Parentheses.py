class Solution:
    def isValid(self, s: str) -> bool:
        if s is None or len(s)==0:
            return True
        stack=[]
        for i in s:
            if i=='(':
                stack.append(')')
            elif i=='{':
                stack.append('}')
            elif i=="[":
                stack.append(']')
            elif len(stack)==0 or stack.pop()!=i:
                return False
        return len(stack)==0
if __name__ == "__main__":
    x=Solution()
    print(x.isValid("{}{}[]"))