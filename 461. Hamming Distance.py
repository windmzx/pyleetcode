class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x= x^y
        res=0
        while x>0:
            res+=x&1
            x=x>>1
        return res
if __name__ == "__main__":
    x=Solution()
    print(x.hammingDistance(1,4))