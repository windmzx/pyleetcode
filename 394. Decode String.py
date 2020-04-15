class Solution:
    def decodeString(self, s: str) -> str:
    # s = "3[a]2[bc]", return "aaabcbc".
    # s = "3[ ]", return "accaccacc".
    # s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
        stack1=[]
        stack2=[]
        num=0
        st=""
        for i in s:
            m=ord(i)
            # 是字母
            
            if (m>=65 and m<=90 )or (m>=97 and m<=122):
                st+=i
            elif i=='[':
                stack2.append(num)
                stack1.append(st)
                num=0
                st=""
            elif i==']':
                # 右括号开始构建字符串
                times=stack2.pop()
                while times>0:
                    stack1[-1]=stack1[-1]+st
                    times-=1
                st=stack1[-1]
                stack1.pop()

            else:
                num=num*10+int(i)


        return st
if __name__ == "__main__":
    x=Solution()
    re=x.decodeString("3[a2[c]]")
    print(re)